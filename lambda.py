# Lambda function or anonymous function
# minus = lambda x,y:x-y
# print(minus(9,4))

# sort function

# def a_first(a):
#     return a[1]
#
# a =[[1,4],[5,2],[2,3]]
# a.sort(key=a_first)
# print(a)

# using lambda

a =[[1,4],[5,2],[2,3]]
a.sort(key=lambda x:x[0])
print(a)