from random import randrange
from game_constants import RULES

RULES = RULES["progression"]


def game_logic():
    first_num = randrange(5, 10)
    last_num = randrange(40, 50)
    step = randrange(3, 6)

    progression = list(range(first_num, last_num, step))

    random_index = randrange(len(progression))
    win_txt = str(progression[random_index])
    progression[random_index] = '..'

    nums = " ".join(map(str, progression))
    return win_txt, nums
