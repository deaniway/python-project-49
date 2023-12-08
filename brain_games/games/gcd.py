from brain_games.random_utilits import generate_number
from math import gcd
from brain_games.engine import run_game
from brain_games.game_constants import GAME_INSTRUCTIONS


def get_gcd(first_num, second_num):
    return str(gcd(first_num, second_num))


def generate_and_calculate_expression_result():
    first_num, last_num = generate_number(), generate_number()
    gcd = get_gcd(first_num, last_num)
    nums = f'{first_num} {last_num}'

    return nums, gcd


def run_gcd_game():
    run_game(generate_and_calculate_expression_result, GAME_INSTRUCTIONS["gcd"])
