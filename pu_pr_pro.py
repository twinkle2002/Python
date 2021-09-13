# Public
# Protected
# Private

class Employee:
    no_of_leaves = 8
    var = 8
    _protect = 5
    __private = 99

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


emp = Employee("murat", 456, "programmer")
print(emp._Employee__private)
print(emp._protect)
print(emp.var)  #public







