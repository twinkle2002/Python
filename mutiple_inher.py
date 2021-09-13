class Employee:
    no_of_leaves = 8
    var = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"name is {self.name}. salary is {self.salary}. and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
         print("this is good" + string)
#
#     return cls(*string.split("-"))


class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"name is {self.name}. game is {self.game}"

class CoolProgrammer(Employee, Player):
    # var = 10
    language = "c++"
    def printlanguage(self):
        print(self.language)

murat = Employee("Murat", 4500, "Instructor")
ahaan = Employee("Ahaan", 4554, "Student")


hayat = Player("Hayat", ["football"])
twink = CoolProgrammer("twink", 8999, "CoolProgrammer")
# det = twink.printdetails()
# twink.printlanguage()
# print(det)

print(twink.var)







