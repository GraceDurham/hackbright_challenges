
def max_num(num_lst):
    """Returns largest integer from a list"""

    max_int = num_lst[0]
    #grab number at beginning of list save to variable max int
    print max_int

    for num in num_lst:

        if num > max_int:
            max_int = num

    return max_int


print max_num([5, 3, 6, 2, 1])