from random import randrange
from brain_games.game_constants import RULES

RULES = RULES["prime"]


def game_logic():

    num = randrange(2, 50)
    win_txt = 'yes' if is_prime(num) else 'no'
    return win_txt, num


def is_prime(nums):
    con = 0
    for i in range(2, nums // 2 + 1):
        if nums % i == 0:
            con += 1
    if con <= 0:
        return True
    else:
        return False
