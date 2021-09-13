# def function1():
#     print("subscribe now")
#
# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
# a = funcret(1)
# print(a)

# def executor(func):
#     func("this")
# executor(print)

def dec1(func1):
    def nowexe():
        print("executing now")
        func1()
        print("executed")
    return nowexe

@dec1
def who_is_twink():
    print("twink is a good girl")

# who_is_twink = dec1(who_is_twink)
who_is_twink()