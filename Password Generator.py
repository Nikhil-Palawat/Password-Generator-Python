import random
import string

def generate_password(length=12):
    # Define character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Combine all character sets
    all_characters = upper + lower + digits + special

    # Ensure at least one character from each set is included
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special),
    ]

    # Fill the remaining length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    # Join the list into a string
    return ''.join(password)

# Generate a password of default length 12
if __name__ == "__main__":
    print("Generated Password:", generate_password())
