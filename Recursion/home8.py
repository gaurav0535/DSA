def fun(a,n):
    x = 0
    if (n==1):
        return a[0]
    else:
        x = fun(a,n-1)
    if (x>a[n-1]):
        return x
    else:
        return a[n-1]

a = [12,10,30,50,100]
print(fun(a,5))

print(int(1/2))
