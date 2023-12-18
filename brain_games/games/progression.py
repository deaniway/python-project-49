from brain_games.utils import generate_rand_num
from brain_games.constants import GAME_INSTRUCTIONS, PROGRESSION_LENGTH
from brain_games.engine import run_game


def generate_progression(start, step, length):
    return list(range(start, start + step * length, step))


def generate_progression_question():

    start_num, step = generate_rand_num(), generate_rand_num()
    progression = generate_progression(start_num, step, PROGRESSION_LENGTH)

    index_to_replace = generate_rand_num(0, PROGRESSION_LENGTH - 1)
    correct_answer = progression[index_to_replace]
    progression[index_to_replace] = '..'

    nums = " ".join(map(str, progression))
    return nums, str(correct_answer)


def run_progression_game():
    run_game(generate_progression_question, GAME_INSTRUCTIONS["progression"])
