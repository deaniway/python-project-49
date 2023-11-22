import random
from brain_games.random_utilits import generate_number
from brain_games.engine import run_game
from brain_games.game_constants import GAME_INSTRUCTIONS


def calculate_expression_and_get_result():
    first_num, last_num = generate_number(), generate_number()
    actions = ['+', '-', '*']

    action = random.choice(actions)
    result = eval(f'{first_num} {action} {last_num}')
    expression = f'{first_num} {action} {last_num}'

    return expression, str(result)


def run_calc_game():
    run_game(calculate_expression_and_get_result, GAME_INSTRUCTIONS["calc"])
