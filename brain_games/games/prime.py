from brain_games.utils import generate_random_number
from brain_games.engine import run_game
from brain_games.constants import GAME_INSTRUCTIONS


def is_prime(nums):
    con = 0
    for i in range(2, nums // 2 + 1):
        if nums % i == 0:
            con += 1
    if con <= 0:
        return True
    else:
        return False


def get_number_and_prime_answer():

    num = generate_random_number()
    correct_answer = 'yes' if is_prime(num) else 'no'
    return num, correct_answer


def run_prime_game():
    run_game(get_number_and_prime_answer, GAME_INSTRUCTIONS["prime"])
