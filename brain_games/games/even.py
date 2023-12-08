from brain_games.random_utilits import generate_number
from brain_games.engine import run_game
from brain_games.game_constants import GAME_INSTRUCTIONS


def is_even(num):
    return num % 2 == 0


def generate_number_and_evenness_answer():
    num = generate_number()
    correct_answer = 'yes' if is_even(num) else 'no'
    return num, correct_answer


def run_even_game():
    run_game(generate_number_and_evenness_answer, GAME_INSTRUCTIONS["even"])
