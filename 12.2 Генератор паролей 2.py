from random import sample, choice
import string

def generate_password(length):
    elements = string.ascii_letters + string.digits
    upper_letter = choice(string.ascii_uppercase.replace('I', '').replace('O', ''))
    lower_letter = choice(string.ascii_lowercase.replace('l', '').replace('o', ''))
    digit = choice(string.digits.replace('0', '').replace('1', ''))
    all_symbols = upper_letter + lower_letter + digit
    return ''.join(sample([i for i in elements if i not in ['l','I','1','0','o','O']], length-3)) + all_symbols

def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())
if __name__=="__main__":
    generate_passwords(n, m)