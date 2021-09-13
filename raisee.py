a = input("what is your name")
b = input("how much do you earn")
if b==0:
    raise ZeroDivisionError("B is 0 so stopping program")

if a.isnumeric():
    raise Exception("numbers are not allowed")

print(f"hello {a}")
# 1000 lines taking 1 hour

c = input()
try:
    print(a)

except Exception as e:
    if c=="twink":
        raise ValueError("twink is blocked she is not allowed")

    print("Exception handled")