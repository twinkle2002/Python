n = int(input("how many rows you want \n "))

print("enter 1 or 0 \n")
bool_val = input("1 for true or 0 for false: ")

if bool_val=="1":
    for i in range(0, n+1):
         print("*" * i)
elif bool_val =="0":
    for i in range(n, 0, -1):
         print("*" * i)