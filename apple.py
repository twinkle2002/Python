n = int(input("Enter the number of apple snowhite got \n"))
mx = int(input("Enter the maximum number \n"))
mn = int(input("Enter the minimum number \n"))

for i in range(mn, mx+1):
    if n%i == 0:
        print(f"{i} is divisor of {n}")
    else:
        print(f"{i} is not divisor of {n}")

if mn == mx:
    print("This is not a range \n")
    if n%mn == 0:
        print("mn or mx is divisor of n \n")
        exit()





