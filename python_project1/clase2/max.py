list1 = [3, 4, 5, 7, 11, 456, 3]
print(min(list1))


def even(x): 
    return x % 2 == 0

print(even)
myEven = even
print(myEven(5))

print(list(filter(myEven, list1)))