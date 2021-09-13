import json

data = '{"var1":"hayat", "var2":56}'

parsed = json.loads(data)
print(parsed['var1'])

# parsed = json.load(data)

data2 = {
    "happy_me":"smileandroll",
    "cars":['bmw', 'audi a8', 'ferrari'],
    "fridge": ("cock", 2),
    "isbad": False
}

jscomp = json.dump(data2)
print(jscomp)