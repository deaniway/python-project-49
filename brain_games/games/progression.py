from random import randrange
from brain_games.game_constants import GAME_INSTRUCTIONS
from brain_games.engine import run_game


def generate_number_progression():

    first_num = randrange(5, 10)
    last_num = randrange(40, 50)
    step = randrange(3, 6)

    return first_num, last_num, step


def math_expression_and_result():
    
    first_num, last_num, step = generate_number_progression()

    progression = list(range(first_num, last_num, step))

    random_index = randrange(len(progression))
    correct_answer = str(progression[random_index])
    progression[random_index] = '..'

    nums = " ".join(map(str, progression))
    return nums, correct_answer


def run_progression_game():
    run_game(math_expression_and_result, GAME_INSTRUCTIONS["progression"])
