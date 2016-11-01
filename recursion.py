def recursion(list):
    if list == '':
        return 0
    else:
        return 1 + recursion(list[:-1])


print recursion("harshdeep")