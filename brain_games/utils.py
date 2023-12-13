import random


def generate_random_number():
    return random.randint(2, 20)


def generate_number(num):
    return random.randrange(num)


def generate_progression(start, step, length):
    return list(range(start, start + step * length, step))
