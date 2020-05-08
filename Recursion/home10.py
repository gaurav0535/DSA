def fun(a,b):
    #print(a,b)
    if (b == 0):
        return 0
    if (b%2 == 0):
        return (a+a,int(b/2))

    return fun(a+a,int(b/2)) + a


print(fun(4,3))