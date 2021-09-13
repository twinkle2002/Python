#a=8
#b=5
#c=sum((a,b))  # built in function\
#print(c)


def function1(a,b):
    print("you are in function", a+b)
function1(4,3)

def function2(c,d):
    """This is a function which calculate averagr"""
    avg = (c+d)/2
    print(avg)
    return avg

v = function2(12,4)
print(v)

print(function2.__doc__)


