
def con_cate(lst1, lst2):
    """returns a single list by concatenating the two lists"""

    for num in lst2:
        lst1.append(num)

    return lst1
print con_cate([1,2],[3,4])