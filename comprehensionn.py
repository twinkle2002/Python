# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

ls = [i for i in range(100) if i%3==0]

print(ls)

# {0:"item0", 1:"item1"}
# dict1 = {i:f"item{i}" for i in range(1, 100) if i%100==0}
dict1 = {i:f"item{i}" for i in range(5)}

dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n", dict2)

"{}" used for list
dresses = {dress for dress in ["dress1", "dress2", "dress1",
                               "dress2","dress1", "dress2"]}
print(dresses)
print(type(dresses))

# "()" used for generator
evens = (i for i in range(100) if i%2==0)
print(type(evens))
print(evens.__next__())
print(evens.__next__())

for item in evens:
    print(item)
