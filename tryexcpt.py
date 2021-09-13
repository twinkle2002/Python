num1 = input("enter num1 \n")
num2 = input("enter num2 \n")
try:
    print("the sum is", int(num1) + int(num2))
except Exception as tw:
    print(tw)

print("this line is important")