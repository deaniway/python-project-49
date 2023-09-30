from random import randrange, choice


def game_logic():

    print('What is the result of the expression?')
    first_num = randrange(10)
    last_num = randrange(10)
    action = choice(list({'+', '-', '*'}))

    if action == '+':

        nums = f'{first_num} + {last_num}'
        win_txt = str(first_num + last_num)
        return win_txt, nums

    if action == '-':

        nums = f'{first_num} - {last_num}'
        win_txt = str(first_num - last_num)
        return win_txt, nums

    if action == '*':

        nums = f'{first_num} * {last_num}'
        win_txt = str(first_num * last_num)
        return win_txt, nums
