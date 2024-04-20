import time
from openai import OpenAI
from getChatMessages import global_user, global_message
import time

def respondToMessage(user, message):
    def api_call(message):
        client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

        completion = client.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "system",
                 "content": "You are in a Livestream and you want to answer to a message in a colloquial way. You can either rewrite the message in a different way and act like you wanted to say the same thing or write something of your own that fits into the context"},
                {"role": "user", "content": message}
            ],
            temperature=0.7,
        )
        return completion.choices[0].message.content

    result = api_call(message)

    # Respond to Message
    time.sleep(5)
    print(f"@{user} {result}")
