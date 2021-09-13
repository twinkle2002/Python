import re

mystr = """sddhbnk mnjhgjh bjhk
nkmlm.,
jhuhuh
fasss
"""


# patt = re.compile(r'fass')
# patt = re.compile(r'.adm')
# patt = re.compile(r'^juhhuh')
# patt = re.compile(r'juhhuh$')
# patt = re.compile(r'as*')
# patt = re.compile(r'a*i*')
# patt = re.compile(r'as+')
# patt = re.compile(r'as{2}')
# patt = re.compile(r'(as){1}')
patt = re.compile(r'(as){1}|fasss')
# patt = re.compile(r'\Afass')
patt = re.compile(r'fass\b')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
    print(mystr[448:452])
