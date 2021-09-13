print("Enter the numbers of the list one by one \n")
size = int(input("Enter size of list \n"))

mylist = []
for i in range(size):
    mylist.append(int(input("Enter list element \n")))

print(f"Your list is {mylist} \n")

reverse1 = mylist[:]
reverse1.reverse()
print(f"First reverse list of {mylist} and {reverse1}")

reverse2 = mylist[::-1]
print(f"Second reverse list is {reverse2}")

reverse3 = mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3) - i - 1] = reverse3[len(reverse3) -i - 1], reverse3[i]

print(f"Third reverse list is {reverse3} \n")

if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods give the same result")
