from random import randint, choice
import operator
from brain_games.engine import run_game
from brain_games.game_constants import GAME_INSTRUCTIONS


def generate_number():
    return randint(0, 9)


def operators_generate():
    first_num = generate_number()
    last_num = generate_number()

    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul
                 }
    return first_num, last_num, operators


def math_expression_and_result():

    first_num, last_num, operators = operators_generate()
    action = choice(list(operators.keys()))
    expression = f'{first_num} {action} {last_num}'
    correct_answer = str(operators[action](first_num, last_num))

    return expression, correct_answer


def run_calc_game():
    run_game(math_expression_and_result, GAME_INSTRUCTIONS["calc"])
