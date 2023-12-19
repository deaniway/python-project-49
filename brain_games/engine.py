import prompt
from brain_games.constants import MAX_ROUND


def run_game(get_question_and_answer, instruction):
    user_name = prompt.string(
        'Welcome to the Brain Games!\n'
        'May I have your name? '
    )

    print(f"Hello, {user_name}\n"
          f"{instruction}")

    for _ in range(MAX_ROUND):
        question, correct_answer = get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\n'
                                    'Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
