from brain_games.cli import welcome_user


def run_game(get_question_and_answer, instruction):
    user = welcome_user()

    print(instruction)

    con = 0
    for _ in range(3):
        question, correct_answer = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            con += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user}!")
            break
    if con == 3:
        print(f'Congratulations, {user}!')
