def digitize(n):

    digit = str(n)

    array =  map(int,digit)
    return array[::-1]

digitize(1234)