"""

Given a non-empty sequence of characters, return true if sequence is Binary, else return false

"""


def isBinary(str):
    for i in str:
        if int(i) != 1 and int(i) != 0:
            return 0

    return 1



print(isBinary("12"))



