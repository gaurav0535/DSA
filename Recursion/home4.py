def fun1(n):
    i = 0
    if n > 1:
        fun1(n-1)

    for i in range(n):
        print("*")


fun1(5)
