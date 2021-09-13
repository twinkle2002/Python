class Employee:
    no_of_leaves = 8
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"name is {self.name}. salary is {self.salary}. and role is {self.role}"


murat = Employee("Murat",4500,"Instructor")
ahaan = Employee("Ahaan",4554,"Student")

# murat.name = "Murat"
# murat.salary = 455
# murat.role = "Instructor"
# ahaan.name = "Ahaan"
# ahaan.salary = 4554
# ahaan.role = "Student"

# print(murat.printdetails())
print(murat.salary)