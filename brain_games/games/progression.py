from brain_games.utils import generate_number, generate_random_number
from brain_games.constants import GAME_INSTRUCTIONS, PROGRESSION_LENGTH
from brain_games.engine import run_game


def generate_progression(start, step, length):
    return list(range(start, start + step * length, step))


def calculate_expression_and_result():
    start_num = generate_random_number()
    step = generate_random_number()

    progression = generate_progression(start_num, step, PROGRESSION_LENGTH)

    index_to_replace = generate_number(len(progression))
    correct_answer = progression[index_to_replace]
    progression_with_dots = progression.copy()
    progression_with_dots[index_to_replace] = '..'

    nums = " ".join(map(str, progression_with_dots))
    return nums, str(correct_answer)


def run_progression_game():
    run_game(calculate_expression_and_result, GAME_INSTRUCTIONS["progression"])
