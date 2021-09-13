def searcher():
    import time
    # some 4 seconds time consuming task
    book = "this is a book with hayat and murat hayat good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in book")
        else: print("Your text is not in book")

search = searcher()    #coroutine
print("search started")
next(search)
print("next method run")
search.send("hayat")
input("press any key")
search.send("murat")
input("press any key")
search.send("joker")

search.close()