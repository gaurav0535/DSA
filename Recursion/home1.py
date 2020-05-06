def func1(x,y):
    #print(x, y)
    if x == 0:
        print(y)
        return y

    else:

        return func1(x-1,x+y)



print(func1(5,5))