import random
from API_Call import api_call


def WriteOwnMessage():
    prompts = [
        "Imagine you are inside of a Lofi Livestream and you want to write something nice inside the Chat. Your message should be short and colloquial written. Do not use any hastags # and keep it simple. Focus on the here and now, do not talk about the future.",
        "Imagine you are inside of a Livestream for Studymusic and you want to write inside the Chat. Write a Hashtag # message related to one of these Things: Studying, being Productive, Concentrating, Good Vibes, good Energy, etc..."
    ]
    promptnumber = random.randint(0, len(prompts) - 1)
    user_input = api_call(prompts[promptnumber])
    return user_input


