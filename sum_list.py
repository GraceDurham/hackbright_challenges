

def sum_list(lst):
    """Returns the number from summing all the numbers in a list"""

    sums = 0

    for num in lst:
        sums = sums + num
        print num, 
        print sums
    
    return sums


print sum_list([5, 3, 6, 2, 1])