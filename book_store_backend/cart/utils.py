import string
import random


def str_generator(size=10, generate_number=False):
    if generate_number:
        chars = string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(size))
