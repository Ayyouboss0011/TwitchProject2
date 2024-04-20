import random
import string

# Define the characters to use in the password
characters = string.ascii_letters + string.digits  # lowercase letters, uppercase letters, and digits

# Generate a random password with 10 characters
password_length = 10
generated_password = ''.join(random.choice(characters) for _ in range(password_length))

# Print and store the generated password
print("Generated Password:", generated_password)

# If you want to use the generated password in your code, you can access it via the 'generated_password' variable.

