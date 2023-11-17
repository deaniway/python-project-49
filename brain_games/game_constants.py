GAME_INSTRUCTIONS = {

    "even": '''Answer "yes" if the number is even, otherwise answer "no".''',
    "calc": 'What is the result of the expression?',
    "gcd": 'Find the greatest common divisor of given numbers.',
    "progression": 'What number is missing in the progression?',
    "prime": '''Answer "yes" if given number is prime. Otherwise answer "no".''',

}

MAX_ROUND_GAME = 3

ERROR_MESSAGE = (
    f"'{{user_answer}}' is wrong answer ;(."
    f" Correct answer was '{{correct_answer}}'.\n"
    f" Let's try again, {{user_name}}!"
)
