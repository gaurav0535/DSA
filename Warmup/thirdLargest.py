# You are required to complete this method
# Just Return 3rd Largets integer from the list
# arr Integer List, n Size of the List
# You may use module's
def thirdLargest(arr, n):
    max = 0
    secondLargest = 0
    thirdLargest = -1
    count = 0
    for i in arr:
        if i > max:
            thirdLargest = secondLargest
            secondLargest = max
            max = i

        elif i > secondLargest:
            thirdLargest = secondLargest
            secondLargest = i

        elif i > thirdLargest:
            thirdLargest = i
        count = count + 1

    if count < 3:
        return -1
    return thirdLargest


# {
#  Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(thirdLargest(arr, n))
# Contributed by: Harshit Sidhwa
# }