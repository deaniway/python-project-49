import prompt


def run_game(get_question_and_answer, instruction):

    user_name = prompt.string('Welcome to the Brain Games!\n'
                              'May I have your name? ')
    print(f"Hello, {user_name}")
    print(instruction)

    max_round_game = 3

    for _ in range(max_round_game):
        question, correct_answer = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')

        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
