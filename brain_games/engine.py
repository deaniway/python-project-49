from brain_games.cli import welcome_user


def engie(game):

    user = welcome_user()
    CON = 0

    while CON < 3:

        win_answer, numbers = game.game_logic()
        print(f'Question: {numbers}')
        u_answer = str(input('Your answer: '))

        if u_answer == win_answer:
            CON += 1
            print('Correct!')
        else:
            print(f'{u_answer} is wrong answer ;(.'
                  f'Correct answer was {win_answer}')
            print(f"Let's try again, {user}!")
            break
    if CON == 3:
        print(f'Congratulations, {user}!')

# обратить внимание общее в грах в строй весии кода тк движка нет (c)Рафи
