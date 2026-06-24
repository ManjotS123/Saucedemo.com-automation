import random
import string

def first_name(length):
    for i in range(length):
        return ''.join(random.choice(string.ascii_letters))



def last_name(length):
    for i in range(length):
        return ''.join(random.choice(string.ascii_letters))



def postal_code(length):
    for i in range(length):
        return ''.join(random.choice(string.digits))

