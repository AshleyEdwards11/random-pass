import random
import string

def generate_password(length, complexity):
    """
    Generate a random password with user-specified length and complexity.
    :param length: int, the desired length of the password
    :param complexity: int, the desired complexity of the password
    :return: str, the generated password
    """
    # define the possible characters for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # create a list of characters based on the desired complexity
    characters = lowercase
    if complexity >= 2:
        characters += uppercase
    if complexity >= 3:
        characters += digits
    if complexity >= 4:
        characters += special

    # generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Example usage
length = 16
complexity = 4
print(generate_password(length, complexity))
