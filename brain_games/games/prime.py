from brain_games.utils import generate_rand_num
from brain_games.engine import run_game
from brain_games.constants import GAME_INSTRUCTIONS


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_number_and_prime_answer():

    num = generate_rand_num()
    answer = 'yes' if is_prime(num) else 'no'
    return num, answer


def run_prime_game():
    run_game(get_number_and_prime_answer, GAME_INSTRUCTIONS["prime"])
