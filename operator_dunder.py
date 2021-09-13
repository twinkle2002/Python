class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):  #Dunder method
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"name is {self.name}. salary is {self.salary}. and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):  #used for operator overloading
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee ({self.name}, {self.salary}, {self.role})"

    def __str__(self):
        return f"name is {self.name}. salary is {self.salary}. and role is {self.role}"

emp1 = Employee("Murat", 956, "student")
# emp2 = Employee("Doruk", 756, "Programmer")
print(emp1)


# mapping operator google







