class Employee:
    no_of_leaves = 8
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"name is {self.name}. salary is {self.salary}. and role is {self.role}"

    # classmethod
    # def change_leaves(cls, newleaves):
    #     cls.no_of_leaves = newleaves

    classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

murat = Employee("Murat",4500,"Instructor")
ahaan = Employee("Ahaan",4554,"Student")
noel = Employee.from_dash("noel-456-student")

# murat.change_leaves(34)
# print(murat.printdetails())
# print(murat.no_of_leaves)
print(noel.salary)



# 57th vedio