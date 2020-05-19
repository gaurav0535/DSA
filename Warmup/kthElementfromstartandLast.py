def kthElement(arr,n):
    print(len(arr))
    print(n)
    if len(arr) > n:
        temp = arr[n]
        arr[n] = arr[len(arr)-n]
        arr[len(arr) - n] = temp
        return arr
    else:
        print(len(arr))
        print(n)
        print("given kth element position is greater than the complete array")

temp = [1,2,3,4,5,6]

print(kthElement(temp,2))

