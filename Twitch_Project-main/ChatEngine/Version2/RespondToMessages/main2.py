import random
from getChatMessages import getChatMessages
from respondToChatMSG import respondToMessage
# List of words to avoid in messages
words_to_avoid = ["subscribed", "resubscribed", "Prime", "months", "month", "sub", "subs", "gifted"]

while True:
    user, message = getChatMessages()

    # Check if any of the words to avoid are present in the message
    if not any(word in message for word in words_to_avoid):
        coinflip = random.randint(1, 4)
        if coinflip == 1:
            respondToMessage(user, message)