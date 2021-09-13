numbers = ["3", "34", "64"]
numbers = list(map(int, numbers))
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
# print(numbers[2])

# def sq(a):
#     return a*a
#
# num = [2,5,3,55,8,56,4,6,8]
# square = list(map(sq,num))
# print(square)

# num = [2,5,3,55,8,56,4,6,8]
# square = list(map(lambda x:x*x,num))
# print(square)


# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func = [square , cube]
# for i in range(5):
#     val = list(map(lambda x:x(i),func))
#     print(val)

# filter function
list_1 = [1,2,3,4,5,6,7,8,9]
def is_greater_5(num):
    return num>5

gr_than_5 = list(filter(is_greater_5, list_1))
print(gr_than_5)


# reduce function
from functools import reduce

list1 = [1,2,3,4]
num = reduce(lambda x,y:x+y, list1)
mul = reduce(lambda x,y:x*y, list1)
print(num)
print(mul)