import random
import string

def generate_password(length):
    # Define the characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example: Generate a random password of length 16
len = int(input("Enter the length of password you want to create: "))
random_password = generate_password(len)
print(random_password)
