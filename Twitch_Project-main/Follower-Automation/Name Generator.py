import random
import pandas as pd

# Load the CSV file with names
names_df = pd.read_csv('/home/ubuntu/Desktop/Twitch BOT/Gamertags.csv')

# Function to generate gamer-style usernames within the length range and without spaces
def generate_gamer_username(name, min_length=4, max_length=25):
    modifiers = ["xX", "Pro", "Epic", "The", "Shadow", "Ninja", "Gamer", "Sniper", "Noob", "Cyber"]
    separator = random.choice(["_", "-", ""])

    parts = name.split(" ")  # Split name into parts
    if len(parts) >= 2:
        part1 = parts[0]
        part2 = parts[-1]
    else:
        part1 = parts[0]
        part2 = random.choice(names_df['Name'])

    modifier = random.choice(modifiers)

    # Generate a username with a limited number of attempts
    max_attempts = 100  # Adjust as needed
    for _ in range(max_attempts):
        username = f"{modifier}{part1}{separator}{part2}"
        username = username.replace(" ", "")  # Remove spaces
        if min_length <= len(username) <= max_length:
            return username

    # If no valid username is generated within the allowed attempts, return an empty string
    return ""

# Generate gamer-style usernames
num_usernames = 10  # Change this to the number of usernames you want to generate
usernames = []
for _ in range(num_usernames):
    random_name = random.choice(names_df['Name'])
    gamer_username = generate_gamer_username(random_name, min_length=4, max_length=25)
    usernames.append(gamer_username)

# Print the generated usernames
for username in usernames:
    print(username)

