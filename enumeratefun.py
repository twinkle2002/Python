l1 = ["cake", "pastry", "chocolate", "ice-creame"]

# i=1
# for item in l1:
#     if i%2 != 0:
#         print(f"jarvis please buy {item}")
#     i +=1

# enumerate function

for index, item in enumerate(l1):
    if index%2==0:
        print(f"jarvis please buy {item}")