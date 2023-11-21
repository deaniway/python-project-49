import random
import operator
from brain_games.random_utilits import generate_random_number
from brain_games.engine import run_game
from brain_games.game_constants import GAME_INSTRUCTIONS


def operators_generate():
    first_num, last_num = generate_random_number(), generate_random_number()
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    action = random.choice(list(operators.keys()))
    selected_operator = operators[action]
    return first_num, last_num, action, selected_operator


def calculate_expression_and_get_result():

    first_num, last_num, action, selected_operator = operators_generate()
    expression = f'{first_num} {action} {last_num}'
    correct_answer = selected_operator(first_num, last_num)

    return expression, str(correct_answer)


def run_calc_game():
    run_game(calculate_expression_and_get_result, GAME_INSTRUCTIONS["calc"])
