from random import randrange

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_logic():

    nums = randrange(2, 50)
    check = check_nums(nums)
    if check is True:
        win_txt = 'yes'
        return win_txt, nums
    else:
        win_txt = 'no'
        return win_txt, nums


def check_nums(nums):
    con = 0
    for i in range(2, nums // 2 + 1):
        if nums % i == 0:
            con += 1
    if con <= 0:
        return True
    else:
        return False
