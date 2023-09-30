from math import gcd
from random import randrange

RULES = 'Find the greatest common divisor of given numbers.'


def game_logic():
    first_num = randrange(10)
    last_num = randrange(10)

    nums = f'{first_num} {last_num}'
    win_txt = str(gcd(first_num, last_num))

    return win_txt, nums
