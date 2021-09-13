class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@happy.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname== None or self.lname == None:
            return "Email is not set please set it using setter"

        return f"{self.fname}.{self.lname}@happy.com"

    @email.setter
    def email(self, string):
        print("setting now...")
        names = string.split("@") [0]
        self.fname = names.split(".") [0]
        self.fname = names.split(".") [1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

Shining_Star = Employee("Shining", "Star")
Hande_Miyy = Employee("Hande", "Miyy")

print(Shining_Star.email)

Shining_Star.fname = "Twinkle"
print(Shining_Star.email)
Shining_Star.email = "this.that@happy.com"
print(Shining_Star.fname)

del Shining_Star.email
print(Shining_Star.email)
Shining_Star.email= "Hande.Miyy@happy.com"
print(Shining_Star.email)

