
class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBook(self):
        print(f"We have following books in our library:{self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self, book, user):
        if book not in self.lendDict.keys():
            self.lendDict.update({book, user})
            print("Lender-Book database has been updated.You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print("Book has been added to the booklist")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    twink = Library(['Cinderella', 'Snow-white', 'TinkerBell', 'Repunzel', 'Eda', 'Hayat'],
    "Dream-catcher")

    while(True):
        print(f"Welcome to the {twink.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book")
        user_choice = int(input())
        if user_choice not in [1,2,3,4]:
            # print("please enter a valid option")
            continue

        # else:
        #     user_choice = int(user_choice)

        if user_choice == 1:
            twink.displayBook()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            name = input("Enter tne name")
            twink.lendBook(book, name)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add")
            twink.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return")
            twink.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quite and c to continue")
        user_choice2 = ""
        while(user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()


