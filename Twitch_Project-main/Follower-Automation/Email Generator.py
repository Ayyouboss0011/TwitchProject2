import itertools

# Function to generate and print email variations with multiple dots inside the email address
def generate_and_print_email_variations(email):
    email = email.lower()  # Make the email lowercase to ensure case insensitivity
    local_part, domain = email.split('@')
    num_chars = len(local_part)

    # Generate and print variations with multiple dots inside the email address
    for num_dots in range(1, num_chars):
        dot_positions = itertools.combinations(range(num_chars), num_dots)
        for positions in dot_positions:
            variation = list(local_part)
            for pos in positions:
                variation.insert(pos, '.')
            generated_email = ''.join(variation) + '@' + domain
            if '..' not in generated_email and not generated_email.startswith('.'):
                print(generated_email)

# Take user input for the email address
email = input("Enter your email address: ")

# Generate and print email variations
generate_and_print_email_variations(email)
