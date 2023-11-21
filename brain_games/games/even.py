from brain_games.random_utilits import generate_number
from brain_games.engine import run_game
from brain_games.game_constants import GAME_INSTRUCTIONS


def is_even(num):
    return num % 2 == 0


def generate_nums_and_correct_answer():
    nums = generate_number()
    return nums, 'yes' if is_even(nums) else 'no'


def run_even_game():
    run_game(generate_nums_and_correct_answer, GAME_INSTRUCTIONS["even"])
