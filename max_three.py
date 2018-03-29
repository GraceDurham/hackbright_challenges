
def max_of_three(num1, num2, num3):
    """Returns largest number out of the three numbers"""

    largest_num = num1

    if num2 >= num1:
        largest_num = num2
    if num3 >= num2:
        largest_num = num3
    if num1 >= num3:
        largest_num = num1


    return largest_num




print max_of_three(5, 11, 31)



def max_three(num1, num2, num3):
    """Return the largest of the three integers"""

    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2


    elif num3 >= num2 and num3 >= num1:
        return num3

    else:
        return "Something went wrong"



print max_three(1, 5, 2)