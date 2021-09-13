import re

str = """
cfgnhg
bdvsvchshxsa
mkejfkr6689ujnvjgk
5tg8tr6glkrnvjtnb86gtmrkemgkrmrk8645vb
kgtrgmvlvjrjgti6gkjgbogkb
ngngitjrr
tdmnjd@gmail.com
hyhkmykhmvylh512uhyh h
Y
hgrykyumnkyumu
gtrmhkytmjnyul
krina16@gmail.com
tmhlymjlu,
bl,hlhlemfrelflfer
g rgtrkhktyhmty
mlhly,lt,
ishita@gmail.com
 tgkdmghkdrmkmkgtm
 ktmdgkbmtkdmhltymnljlk,lhg,bgf,hl,lwdmew6595942g2bgtd gs nthjnkmykmglrla,welmg  kmhktmhkmrdkfmma6gfbjh,lvmriujguthfjrij5865r634hfurehgjg
 hrehfehuegjo
 nvgitg9jioygdqbedjntrkht
 rugjtjr
 twink20@gmail.com
 jtkgjco
 
"""

#email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z0-9]+", str)
email = re.findall(r"\w+@\S+\w+", str)
# \w contain a-z and 0-9
print(email)