
def test_nums_reach_x(nums, target):
    """
    return  the prefix notation of the expression that evaluates to 24
    for example:  3, 8 :  returns [ '*', 3, 8]
    11, 13 : [ ' + ' , 11, 13]

    """
    print("target is ", target , "trying nums :", nums)

    if len(nums) == 1:
        return [] if target != nums[0] else nums

    for i in range(len(nums)):
        new_nums = nums[1:i] + nums[i + 1:]
        print(new_nums)
        coms = get_poss_coms(nums[0], nums[i]) if i != 0 else {nums[0]: nums[0]}
        for a in coms.keys():
            expr2 = coms[a]
            print(f"trying add , with target {target}, a {a}")
            expr1 = test_nums_reach_x(new_nums, target - a)
            if len(expr1) > 0:
                return ['+', expr2, expr1]

            print(f"trying multiple , with target {target}, a {a}")
            if a != 0:
                if target % a == 0:
                    expr1 = test_nums_reach_x(new_nums, target / a)
                    if len(expr1) > 0:
                        return ['*', expr2, expr1]

            print(f"trying subtract  , with target {target}, a {a}")

            expr1 = test_nums_reach_x(new_nums, target + a)
            if len(expr1) > 0:
                return ['-',  expr1, expr2]

            expr1 = test_nums_reach_x(new_nums, a - target)
            if len(expr1) > 0:
                return ['-',  expr2, expr1]

            expr1 = test_nums_reach_x(new_nums, target * a)
            if len(expr1) > 0:
                return ['/',   expr1, expr2]
            if target != 0:
                if a % target == 0:
                    expr1 = test_nums_reach_x(new_nums,  a / target)
                    if len(expr1) > 0:
                        return ['/',  expr2,   expr1]


    return []

def get_poss_coms(a, b):
    coms = {a + b: ('+', str(a), str(b)), max(a, b) - min(a, b): ('-', str(max(a, b)), str(min(a, b))), a * b: ('*', str(a), str(b))}
    if a % b == 0:
        coms[a / b] = ('/', str(a), str(b))
    if b % a == 0:
        coms[b / a] = ('/', str(b), str(a))

    return coms



"""


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
"""


def operate_four(a, b, c, d):
    # see if first  number is a factor of 24, if yes, see other 3 numbers, if  not,
    # try plus or minus or div
    if 24 % a == 0:
        formula = test_nums_reach_x([b, c , d] , 24 / a)
        if formula != []:
            return ['*', a , formula]


    return []



print("Please enter numbers separated by a comma")
s = input()


y =  s.split(',')


nums = [ int(x) for x in y ]

print(test_nums_reach_x(nums, 24))
