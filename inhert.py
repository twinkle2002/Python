class Employee:
     no_of_leaves = 8

     def __init__(self, name, salary, role):
         self.name = name
         self.salary = salary
         self.role = role

     def printdetails(self):
        return f"name is {self.name}. salary is {self.salary}. and role is {self.role}"

    # @classmethod
    # def change_leaves(cls, newleaves):
    #     cls.no_of_leaves = newleaves

     @classmethod

     def from_dash(cls, string):
        return cls(*string.split("-"))

    #  @staticmethod

    # def printgood(string):
    #     print("this is good" + string)
    #
    #     return cls(*string.split("-"))

class programmer(Employee):
      no_of_holiday = 56
      def __init__(self, name, salary, role,languages):
            self.name = name
            self.salary = salary
            self.role = role
            self.role = languages


      def printprog(self):
         return f"  programmer's name is {self.name}. salary is {self.salary}. and role is {self.role}"

murat = Employee("Murat", 4500, "Instructor")
ahaan = Employee("Ahaan", 4554, "Student")

hayat = programmer("hayat", 456, "programmer",["python"])
twink = programmer("twink", 456, "programmer",["python"])

print(twink.no_of_holiday)

# 60th video