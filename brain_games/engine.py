from brain_games.cli import welcome_user


def engie(game, max_attempts=3):
    user = welcome_user()
    print(game.RULES)

    for _ in range(max_attempts):
        win_answer, numbers = game.game_logic()
        print(f'Question: {numbers}')
        u_answer = str(input('Your answer: '))

        if u_answer == win_answer:
            print('Correct!')
        else:
            print(f'{u_answer} is wrong answer ;(.'
                  f'Correct answer was {win_answer}')
            print(f"Let's try again, {user}!")
            break
    else:
        print(f'Congratulations, {user}!')
