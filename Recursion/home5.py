limit = 100

def fun(n):
    if n <= 0:
        return
    if n > limit:
        return
    print(n)
    fun(2*n)
    print(n)


fun(5)