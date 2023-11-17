from math import gcd
from random import randrange
from brain_games.engine import run_game
from brain_games.game_constants import GAME_INSTRUCTIONS


def generate_number_gcd():
    return randrange(10)


def math_expression_and_result():
    first_num = generate_number_gcd()
    last_num = generate_number_gcd()

    correct_answer = str(gcd(first_num, last_num))
    nums = f'{first_num} {last_num}'

    return nums, correct_answer


def run_gcd_game():
    run_game(math_expression_and_result, GAME_INSTRUCTIONS["gcd"])
