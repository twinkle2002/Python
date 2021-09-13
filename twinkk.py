def spy():
    import time
    book = "twink shining hande murat star ask hayat kiraz miyy"
    time.sleep(3)

    while True:
        text = (yield)
        if text in book:
            print("Your name is in list")
        else: print("Your name is not in list")

s = spy()
print("searching......")
next(s)
s.send("hande")
print("again searching..")
s.send("serkan bolat")

