from math import inf
def divide(first, second):
    if second == 0:
        return inf
    return int(first) / int(second)

#print(divide(9, 3))
#print(divide(2, 0))
