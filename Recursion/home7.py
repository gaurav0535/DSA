def fun(n):

    if n > 0:
        fun( n = n - 1)
        print(n)
        fun(n = n - 1)

x = 4
fun(x)