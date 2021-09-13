# Dictionary is nothin but key value pairs
d1  = { }
#print(type(d1))
d2 = {"Hayat":"Burger", "Twinkle":"Pizza", "Krina":"Fries", "ishita":{"B":"maggie", "L":"noodles", "D":"frankie"}}
print(d2["ishita"]["L"])
#d2["Ishqi"] = "junk food"
#d2[424] = "chicken"
#del d2[424]
print(d2)
print(d2.copy())
d3 = d2.copy()
del d2["Hayat"]
print(d2.get("Twinkle"))
d2.update({"sonu":"cake"})
print(d2)
print(d2.keys())
print(d2.items())


# Quize
D = {"p" : "print the element",
"c" : "copy the element",
"m" : "move the element",
"d" : "delete the element"}

code = input("enter the code")
print(D(code))