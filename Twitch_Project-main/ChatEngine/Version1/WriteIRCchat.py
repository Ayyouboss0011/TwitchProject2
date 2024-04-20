import socket

# Twitch IRC server and port
server = 'irc.chat.twitch.tv'
port = 6667

# Twitch username and OAuth token (get your OAuth token from https://twitchapps.com/tmi/)
username = 'waechter4'
token = 'oauth:bw5tok3sxo78mbs9v14yalhtwoqyrp'

# Twitch channel to send messages to
channel = '#Einsamerigel'

def connect():
    global sock
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {username}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

def send_message(message):
    sock.send(f"PRIVMSG {channel} :{message}\n".encode('utf-8'))

if __name__ == "__main__":
    connect()

    while True:
        user_input = input("Enter your message: ")  # Get user input from the terminal
        send_message(user_input)  # Send the user's message to the Twitch channel
