def func(i):
    if (i%2 == 1):
        i = i +1
        return (i)
    else:
        func(func(i-1))

print(func(200))
