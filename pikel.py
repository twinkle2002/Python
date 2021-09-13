import pickle

# picking a python object
# food = ["pizza", "chinese", "samosa", "burger"]
# file = "food.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(food, fileobj)
# fileobj.close()

# it makes one file
file = "food.pkl"
fileobj = open(file, 'rb')
food = pickle.load(fileobj)
print(food)
print(type(food))

# pickel critise do google
