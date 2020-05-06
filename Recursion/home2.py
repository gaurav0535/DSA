def fun(n):
    if n == 1 :
        return 0
    else:
        return 1 + fun(int(n/2))


print(fun(5))