from random import sample
import string
def generate_password(length):
    elements = string.ascii_letters + string.digits
    return ''.join(sample([i for i in elements if i not in ['l','I','1','0','o','O']], length))

def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())
if __name__=="__main__":
    generate_passwords(n, m)