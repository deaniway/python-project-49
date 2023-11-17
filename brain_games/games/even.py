from random import randrange
from brain_games.engine import run_game
from brain_games.game_constants import GAME_INSTRUCTIONS


def generate_random_number():
    return randrange(50)


def is_even(num):
    return num % 2 == 0


def math_expression_and_result():
    nums = generate_random_number()
    return nums, 'yes' if is_even(nums) else 'no'


def run_even_game():
    run_game(math_expression_and_result, GAME_INSTRUCTIONS["even"])
