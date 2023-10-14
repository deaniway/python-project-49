from math import gcd
from random import randrange
from brain_games.game_constants import RULES

RULES = RULES["gcd"]


def game_logic():
    first_num = randrange(10)
    last_num = randrange(10)

    win_txt = str(gcd(first_num, last_num))
    nums = f'{first_num} {last_num}'

    return win_txt, nums
