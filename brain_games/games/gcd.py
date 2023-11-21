from brain_games.random_utilits import generate_number
from math import gcd
from brain_games.engine import run_game
from brain_games.game_constants import GAME_INSTRUCTIONS


def calculate_expression_and_get_result():
    first_num, last_num = generate_number(), generate_number()
    correct_answer = str(gcd(first_num, last_num))
    nums = f'{first_num} {last_num}'

    return nums, correct_answer


def run_gcd_game():
    run_game(calculate_expression_and_get_result, GAME_INSTRUCTIONS["gcd"])
