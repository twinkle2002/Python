import time

initial = time.time()
# print(initial)

k=0
while k<45:
    print("this is murat")
    # time.sleep(2)
    k+=1
print("while loop ran in", time.time() - initial, "seconds")
for i in range(45):
    print("this is murat")
initial2 = time.time()
print("for loop ran in", time.time() - initial2, "seconds")


localtime = time.asctime(time.localtime(time.time()))
print(localtime)  # return time