import socket
import time
import random
from getMessage import WriteOwnMessage


# Twitch IRC server and port
server = 'irc.chat.twitch.tv'
port = 6667

# Twitch usernames (remains constant) and OAuth tokens
username = 'einschoenerhengst'  # Add your username here
tokens = [
    'oauth:xerm1taambwc6aysw9jpfrxwt7qzd6',
    'oauth:vda7h3jc1agqhupsfmtmw3qk1ylffe',
    'oauth:dvcg4bqc5vl9qlnjn92vom6gyinwwr',
    'oauth:8t3196ere5yeinvm7ri1ic7j9my1nc',
    'oauth:bctfidf2h6xgiww3x5le4ko4tmfz5s',
    'oauth:ud2uks739stox4qexbvywyn6x9ywus',
    'oauth:jgedpyhkx4p9fm19xf1t68guqo1xyh',
    'oauth:y6qh54m3hhnebsbwtlfx5tfxs3y0ei',
    'oauth:p4ourua90hzarb7my17uxrhdhjb3km',
    'oauth:7ejgggu3d7ao79scu7covt9kdjikvx',
    'oauth:358azno80ai87v84mgdspywxsxofyz'
]  # OAuth tokens

# Twitch channel to send messages to
channel = '#x'

def connect(username, token):
    global sock
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {username}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

def send_message(message):
    sock.send(f"PRIVMSG {channel} :{message}\n".encode('utf-8'))

if __name__ == "__main__":
    current_token_index = 0
    connect(username, tokens[current_token_index])

    while True:
        user_input = WriteOwnMessage()
        print(user_input)
        send_message(user_input)  # Send the predefined message to the Twitch channel
        random_time = random.randint(1 , 2) # Set Random timeinterval
        # Switch tokens after a certain interval (e.g., every 5 minutes)
        time.sleep(random_time) # Wait random time
        current_token_index = random.randint(0, len(tokens) - 1)
        #current_token_index = (current_token_index + 1) % len(tokens)  # Cycle through tokens
        sock.close()  # Close the current connection
        connect(username, tokens[current_token_index])  # Connect with the new token

