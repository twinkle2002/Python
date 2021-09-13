l=10 # global
def function1(n):
    # l=5  # local variable
    m=8
    global l
    l=l+2
    print(l,m)
    print(n, "i have printed")

function1("this is me")
print(l)


# recursive function
x=90
def hayat():
    x=20
    def murat():
        global x
        x = 88
    # print("before calling murat", x)
    murat()
    print("after calling murat", x)

hayat()
print(x)



