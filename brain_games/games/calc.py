import random
from brain_games.utils import generate_number
from brain_games.engine import run_game
from brain_games.constants import GAME_INSTRUCTIONS, EXPRESSION_ACTIONS


def calculate_result(first_num, second_num, action):
    result = eval(f'{first_num} {action} {second_num}')
    expression = f'{first_num} {action} {second_num}'
    return result, expression


def calculate_expression_and_get_result():
    first_num, second_num = generate_number(10), generate_number(10)
    actions = EXPRESSION_ACTIONS

    action = random.choice(actions)
    result, expression = calculate_result(first_num, second_num, action)
    return expression, str(result)


def run_calc_game():
    run_game(calculate_expression_and_get_result, GAME_INSTRUCTIONS["calc"])
