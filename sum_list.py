# Compute the sum of a list of numbers.


def sum_list(lst):

    sums = 0

    for num in lst:
        sums = sums + num
        print num, 
        print sums
    
    return sums


print sum_list([5, 3, 6, 2, 1])