from random import choice
import string
def generate_index():
    return (f'{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}{choice(string.digits)}_'
            f'{choice(string.digits)}{choice(string.ascii_uppercase)}{choice(string.ascii_uppercase)}')
print(generate_index())