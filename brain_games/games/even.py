from brain_games.utils import generate_rand_num
from brain_games.engine import run_game
from brain_games.constants import GAME_INSTRUCTIONS


def is_even(num):
    return num % 2 == 0


def get_num_and_even_answer():
    num = generate_rand_num()
    correct_answer = 'yes' if is_even(num) else 'no'
    return num, correct_answer


def run_even_game():
    run_game(get_num_and_even_answer, GAME_INSTRUCTIONS["even"])
