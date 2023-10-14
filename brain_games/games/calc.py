from random import randint, choice


def game_logic():
    first_num = randint(0, 9)
    last_num = randint(0, 9)
    operators = {'+': first_num + last_num, '-': first_num - last_num,
                 '*': first_num * last_num
                 }

    action = choice(list(operators.keys()))
    expression = f'{first_num} {action} {last_num}'
    win_txt = str(operators[action])

    return expression, win_txt
