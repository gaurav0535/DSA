def convertFive(n):
    #Code here
    i = 0
    new_num = 0
    while(n > 0):
        i = int(n%10)
        n = int(n/10)

        if (i == 0):
            i = 5
        new_num = str(i)+str(new_num)
    return new_num


print(convertFive(1011232))
