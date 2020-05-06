def fun2(n):
    if n == 0:
        return
    fun2(int(n/2))
    print(int(n%2))


fun2(5)
