def fun(cuont):
    print(cuont)
    if (cuont < 3 ):
        count = cuont + 1
        fun(fun(fun(cuont)))
    return count


fun(1)
