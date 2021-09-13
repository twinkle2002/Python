list1 = [["hayat",5], ["twinkle",2], ["krina",7], ["ishita",258]]
dict1 = dict(list1)
#print(dict1)
for item,cake in dict1.items():
    print(item, "eats this no of", cake)
for item in dict1:
    print(item)

#  Quize
list2 = ["pizza", 7, 3, "maggie", "pasta", 2, 1, 9, 6]
for item in list2:
    if str(item).isnumeric() and item<6:
        print(item)