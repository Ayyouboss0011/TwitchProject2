import socket
import re

# Twitch IRC server and port
server = 'irc.chat.twitch.tv'
port = 6667

# Twitch username and OAuth token (get your OAuth token from https://twitchapps.com/tmi/)
username = 'Einsamerigel'
token = 'oauth:pcephy83m2nva7knml0mjpjxn3ry65'

# Twitch channel to join
channel = '#Einsamerigel'

# Regular expression pattern to parse IRC messages
pattern = re.compile(r'^:(?P<user>[^!]+)![^ ]+ PRIVMSG (?P<channel>[^ ]+) :(?P<message>.+)$')

def connect():
    global sock
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {username}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

def receive_messages():
    while True:
        resp = sock.recv(2048).decode('utf-8')
        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))
        elif len(resp) > 0:
            match = pattern.match(resp)
            if match:
                user = match.group('user')
                message = match.group('message')
                print(f"{user}: {message}")

def send_message(message):
    sock.send(f"PRIVMSG {channel} :{message}\n".encode('utf-8'))

if __name__ == "__main__":
    connect()
    
    # Start a separate thread or process for receiving messages
    # This could be done using threading or multiprocessing modules
    
    # For simplicity, just call receive_messages in the main thread
    receive_messages()

    # Now, we can send messages from the terminal
    while True:
        user_input = input()  # Get user input from the terminal
        send_message(user_input)  # Send the user's message to the IRC channel
