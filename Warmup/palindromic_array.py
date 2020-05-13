def PalinArray(arr ,n):

    for arr in arr:
        old_no = arr
        new_no = 0
        while (arr > 0):
            temp = int(arr%10)
            arr = int(arr/10)
            new_no = new_no*10 + temp

        if new_no == old_no:
            pass
        else:
            return 0

    return


print(PalinArray([12,1,2,3],2))