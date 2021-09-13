# f = open("twinkle.txt", "a")
# a = f.write("twinkle love pizza \n")
# print(a)
# f.close()

# handle read and write both
f = open("twinkle.txt", "r+")
print(f.read())
f.write("thank you")