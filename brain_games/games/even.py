from random import randrange
from game_constants import RULES


RULES = RULES["even"]

def generate_random_number():
    return randrange(50)


def is_even(num):
    return num % 2 == 0


def game_logic():
    nums = generate_random_number()
    return 'yes' if is_even(nums) else 'no', nums
