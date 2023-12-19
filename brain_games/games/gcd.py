from brain_games.utils import generate_rand_num
import math
from brain_games.engine import run_game
from brain_games.constants import GAME_INSTRUCTIONS


def get_gcd(first_num, second_num):
    return math.gcd(first_num, second_num)


def get_number_pair_and_gcd():
    first_num, second_num = generate_rand_num(10), generate_rand_num(10)
    gcd = get_gcd(first_num, second_num)
    nums = f'{first_num} {second_num}'

    return nums, str(gcd)


def run_gcd_game():
    run_game(get_number_pair_and_gcd, GAME_INSTRUCTIONS["gcd"])
