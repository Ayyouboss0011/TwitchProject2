import socket
import time
import random

# Twitch IRC server and port
server = 'irc.chat.twitch.tv'
port = 6667

# Twitch usernames (remains constant) and OAuth tokens
username = 'einschoenerhengst'  # Add your username here
tokens = [
    'oauth:pcephy83m2nva7knml0mjpjxn3ry65',
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
channel = '#Einsamerigel'

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

    messages = [
    "sun​meu primeiro Dorama foi descendentes do sol",
    "MYLENA​quando encontrar um bom me avise",
    "dainis merksons​No i have haracthers its me men i go more",
    "Hannah Kuha​@tbomas did u see it? 😂😂😂 if not that's ok but I can't not over see the convos that your having with cheese and onions, I think it's amazing what you said btw",
    "Floki​i mean",
    "sun​foi lá pr 2019 q eu comecei a assistir",
    "Floki​for real",
    "Outflow ​من وش انضغط أنا كل اللي اسمع لهم من أول عشرة على سبوتيفاي يا ركبة هههههههه",
    "Cheese and Onions​if you love math, you cannot love physics... and vice versa",
    "maybe rohit ​@🤎𝙹𝚒𝚗𝚗𝚢_ why are you typing so slow",
    "Mina​انا ابيه حلو و عنده لسان اوك مب مهم عمره",
    "she​مينا لو تقصديني فا ياااسس جيرلل",
    "sun​tenho uma lista my, dps eu vejo e te falo kkkkkkkkkkk",
    "iPad broken, can’t upload on the og :(​WHAT IS UR OPINION ON 🫒 EMOJI OFFICIAL, BUT SERIOUSLY WHAT IS UR OPINION ON 🫒 EMOJI OFFICIAL, BUT SERIOUSLY WHAT IS UR OPINION ON 🫒 EMOJI OFFICIAL?",
    "MYLENA​ah, não tem na Netflix?",
    "Stark​we can do it keep studyinddjfgo nsdlfbn",
    "Floki​bots are cute"
    "Circus​Vay?",
    "a y​AY AMİN",
    "zehraymis​inşallah çok istedim",
    "Nawalys​antalya çok güzel",
    "Rebellious Goath ​💀🤙🏻",
    "zehraymis​@Circus like wow",
    "a y​senin istediğin bölümm",
    "a y​?",
    "zehraymis​turkish wow",
    "Cemre Geçit​agalar ben yatiyorummm",
    "zehraymis​Circus​SHE ATE ME??",
    "a y​you are so lucky circus",
    "Cemre Geçit​ok circus ok ok",
    "zehraymis​özellikle yokk bilmiyom",
    "zehraymis​eskişehir istiyom ama",
    "Cemre Geçit​im wife her",
    "JAY♤■​boring",
    "Lucas​hiii",
    "Circus​Désolé....",
    "Rebellious Goath ​where are you from N, if you don't mind",
    "Nawalys​iyi geceler ben kaçar",
    "N​Shaqi onil?",
    "N​Im from japan",
    "a y​iyi geceler abii",
    "Reina👑​sureee",
    "onii-chan​reina aw man ik I'm under 6ft that's why i need tall women to help me reach the top shelf",
    "Cemre Geçit​kac kac xy kromozom",
    "Cemre Geçit​iyi geceler xy abi",
    "WHM Productions​im so hony",
    "Rebellious Goath ​oh really cool",
    "Nawalys​iyi geceler xx",
    "Circus​Vay?",
    "a y​AY AMİN",
    "zehraymis​inşallah çok istedim",
    "Nawalys​antalya çok güzel",
    "Rebellious Goath ​💀🤙🏻",
    "zehraymis​@Circus like wow",
    "a y​senin istediğin bölümm",
    "a y​?",
    "zehraymis​turkish wow",
    "Cemre Geçit​agalar ben yatiyorummm",
    "naya_ _cor123💜🖤​كيف عايشة",
    "Hannah Kuha​@thomas nice 😂👍 what are your thoughts on Atheist, I also thought they were a little tricky",
    "Floki​sei la🐳",
    "MYLENA​com requeijão então, melhor refeição.",
    "Mina​ليش مب انسانه",
    "Hannah Kuha​always*",
    "Roj roj​رجاءا مينا هاي نعمة",
    "sun​pse",
    "naya_ _cor123💜🖤​استهبللللل",
    "Roj roj​قولي انك ما تحبيها بس لا تقول اع",
    "Negaless 1​the 2 for 1 foot Ling wow what crooks",
    "Mina​اصلا انا نا اكل وجبة الإفطار وجبه وحده ف اليوم",
    "Negaless 1​see",
    "Negaless 1​hahaa",
    "AfyProjectLab.​hi from Malaysia 🇲🇾🇲🇾🇲🇾",
    "MYLENA​glúten, meu corpo está rejeitando td.",
    ]
    
    while True:
        messagenumber = random.randint(0, len(messages) - 1) # Randomize Message
        user_input = messages[messagenumber]  # Nachricht zum Senden
        send_message(user_input)  # Send the predefined message to the Twitch channel
        random_time = random.randint(3, 5) # Set Random timeinterval
        # Switch tokens after a certain interval (e.g., every 5 minutes)
        time.sleep(random_time) # Wait random time
        current_token_index = random.randint(0, len(tokens) - 1)
        #current_token_index = (current_token_index + 1) % len(tokens)  # Cycle through tokens
        sock.close()  # Close the current connection
        connect(username, tokens[current_token_index])  # Connect with the new token

