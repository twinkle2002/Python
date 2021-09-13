# def function_name_print(a,b,c,d):
#     print(a,b,c,d)
#
# function_name_print("twinkle","hayat","krina","ishita")

def funargs(normal,*argsmurat,**kwargs):
    print(normal)

    for item in argsmurat:
        print(item)

    # for key,value in kwargs.item():
    #     print(key,value)
normal = "this is normal"
har = ["twinkle","hayat","krina","ishita","ishqi"]
# kw = ["krina":"chef"]
funargs(normal,*har)