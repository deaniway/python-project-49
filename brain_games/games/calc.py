from random import randint, choice
from brain_games.game_constants import RULES

RULES = RULES["calc"]


def game_logic():
    first_num = randint(0, 9)
    last_num = randint(0, 9)
    operators = {'+': first_num + last_num, '-': first_num - last_num,
                 '*': first_num * last_num
                 }

    action = choice(list(operators.keys()))
    expression = f'{first_num} {action} {last_num}'
    win_txt = str(operators[action])

    return win_txt, expression
