def show_evens_nums(numbers):
    """Given a list of ints, return list of indices of even numbers in the list"""

    out = []

    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            out.append(i)

    return out



print show_evens_nums([1,2,3,4,6,8])




def show_evens(numbers):
    """Given a list of ints, return list of indices of even numbers in the list."""

    indexes = []

    for index, num in enumerate(numbers):
        if num % 2 == 0:
            indexes.append(index)
    return indexes
    


print show_evens([1,2,3,4,6,8])





















