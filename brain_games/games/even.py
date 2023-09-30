from random import randrange

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_logic():

    nums = randrange(50)
    check = check_nums(nums)
    if check is True:
        win_txt = 'yes'
        return win_txt, nums
    else:
        win_txt = 'no'
        return win_txt, nums


def check_nums(nums):
    if nums % 2 == 0:
        return True
    else:
        return False

# из ревью - проверку вынести отдельно
