import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Get user input for password lenth
password_length = int(input("Enter the desired length of the password:"))

# Generate and display the password
password = generate_password(password_length)
print("Generated Password:", password)