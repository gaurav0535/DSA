"""
Given an sorted array A of size N. Find number of elements which are less than or equal to given element X.
"""


def checSmall(arr,n):
    count = []
    arr = [1,2,3,4,5]
    for i in arr:
        if i < n:
            if i not in count:
                count.append(i)


    return count


test = [1,2,3,4,5]


print(checSmall(test,4))