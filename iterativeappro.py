"""
    :param n: integer
    :return: n * n-1 * n-2 * n-3.......]
    """
# n! = n * n-1 * n-2 * n-3.......]

 # def factorial(n):   # iterative function
    # fac = 1
    # for i in range(n):
    #     fac = fac * (i+1)
    # return fac

# recursive function
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
#     pass
#
# number = int(input("enter the number \n"))
# print(factorial(number))


# Quize
# 0 1 1 2 3 5 8 11......  fibonacci
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    pass


number = int(input("enter the number \n"))
print(fibonacci(number))

