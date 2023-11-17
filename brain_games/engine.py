import prompt
from brain_games.game_constants import MAX_ROUND_GAME, ERROR_MESSAGE


def run_game(get_question_and_answer, instruction):
    user_name = prompt.string('Welcome to the Brain Games!\n'
                              'May I have your name? ')
    print(f"Hello, {user_name}\n" + instruction)

    for _ in range(MAX_ROUND_GAME):
        question, correct_answer = get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')

        if user_answer == correct_answer:
            print('Correct!')

        else:
            error_message = ERROR_MESSAGE.format(user_answer=user_answer,
                                                 correct_answer=correct_answer,
                                                 user_name=user_name)
            print(error_message)
            return

    print(f'Congratulations, {user_name}!')


# давай оставим error_message, мне очень нравится как выглядит,
# так скажем по сеньёрски :)
