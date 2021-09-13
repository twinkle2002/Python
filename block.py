with open("twinkle.txt") as f:
    a = f.read(4)
    print(a)

# after reading the whole file if we again read the file out of with block it will read the file
# f = open("twinkle.txt")
# print(f.readline())
# print(f.readline())
# print(f.readline())

# f.close()