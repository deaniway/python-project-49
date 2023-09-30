from random import randrange, choice

RULES = 'What number is missing in the progression?'


def game_logic():
    first_num = randrange(5, 10)
    last_num = randrange(40, 50)
    step = randrange(3, 6)

    nums = []
    for i in range(first_num, last_num, step):
        nums.append(i)

    random_num = choice(nums)
    index = nums.index(random_num)
    nums[index] = '..'
    win_txt = str(random_num)
    nums = " ".join(map(str, nums))
    return win_txt, nums
