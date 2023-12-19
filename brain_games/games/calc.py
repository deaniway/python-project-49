import random
from brain_games.utils import generate_rand_num
from brain_games.engine import run_game
from brain_games.constants import GAME_INSTRUCTIONS, MATH_SIGNS


def get_math_expression_and_result():
    first_num, second_num = generate_rand_num(10), generate_rand_num(10)
    action = random.choice(MATH_SIGNS)
    expression = f'{first_num} {action} {second_num}'
    result = eval(expression)
    return expression, str(result)


def run_calc_game():
    run_game(get_math_expression_and_result, GAME_INSTRUCTIONS["calc"])
