import socket
import re


global_user = None
global_message = None
def getChatMessages():    # Twitch IRC server and port
    server = 'irc.chat.twitch.tv'
    port = 6667

    # Twitch username and OAuth token (get your OAuth token from https://twitchapps.com/tmi/)
    username = 'coolcert1'
    token = 'oauth:vda7h3jc1agqhupsfmtmw3qk1ylffe'

    # Twitch channel to join
    channel = '#caseoh_'

    # Regular expression pattern to parse IRC messages
    pattern = re.compile(r'^:(?P<user>[^!]+)![^ ]+ PRIVMSG (?P<channel>[^ ]+) :(?P<message>.+)$')

    global sock
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {username}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    while True:
        resp = sock.recv(2048).decode('utf-8')
        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))
        elif len(resp) > 0:
            match = pattern.match(resp)
            if match:
                global_user = match.group('user')
                global_message = match.group('message')
                print(f"{global_user}: {global_message}")
                return global_user, global_message
