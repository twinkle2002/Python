class Employee:
    no_of_leaves = 8
    pass

murat = Employee()
ahaan = Employee()

murat.name = "Murat"
murat.salary = 455
murat.role = "Instructor"
ahaan.name = "Ahaan"
ahaan.salary = 4554
ahaan.role = "Student"
print(ahaan.no_of_leaves)
print(ahaan.__dict__)
Employee.no_of_leaves = 9
ahaan.no_of_leaves = 9
print(ahaan.__dict__)
print(Employee.__dict__)
print(Employee.no_of_leaves)