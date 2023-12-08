import random
from brain_games.engine import run_game
from brain_games.game_constants import GAME_INSTRUCTIONS


def generate_number_and_correct_answer():

    num = random.randrange(2, 50)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return num, correct_answer


def is_prime(nums):
    con = 0
    for i in range(2, nums // 2 + 1):
        if nums % i == 0:
            con += 1
    if con <= 0:
        return True
    else:
        return False


def run_prime_game():
    run_game(generate_number_and_correct_answer, GAME_INSTRUCTIONS["prime"])
