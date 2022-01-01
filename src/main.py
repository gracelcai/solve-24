
def test_nums_reach_x(nums, target):
    """
    return  the prefix notation of the expression that evaluates to 24
    for example:  3, 8 :  returns [ '*', 3, 8]
    11, 13 : [ ' + ' , 11, 13]

    """
    if len(nums) == 1:
        return [] if target != num[0] else nums


    expression = []

    a = nums[0]

    if a * b == 24:
        expression = ['*', a ,b]
    elif a + b == 24:
        expression = ['+', a, b]
    elif  abs(a - b) == 24:
        expression = ['-', max(a, b), min(a, b)]
    elif a / b == 24:
        expression = ['/', a, b]
    elif b / a == 24:
        expression = ['/', b, a]
    else:
        pass

    return expression


def operate_four(a, b, c, d):
    # see if first  number is a factor of 24, if yes, see other 3 numbers, if  not,
    # try plus or minus or div
    if 24 % a == 0:
        formula = test_nums_reach_x([b, c , d] , 24 / a)
        if formula != []:
            return ['*', a , formula]


    return []




def find_24(a, b, c, d):
    pass

def poss_two(a, b):
    return [a * b, a + b, abs(a - b), a / b, b / a]

print("Please enter numbers separated by a comma")
s = input()
nums = [ int(x) for x in s.split(',')]

print(operate_two(nums[0], nums[1]))
