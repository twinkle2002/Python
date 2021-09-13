i = 0

#while(i<45):
 #   print(i)
  #  i = i + 1

# guess the number

# EXERCISE 3

number=18
atmpt = 1

while(atmpt<=4):
     n = int(input("enter the number \n"))
     if n>18:
        print("go towards small number \n")
     elif n<18:
        print("go towards large number \n")
     else:
         print("your guess is correct \n"
               "You Won!!!")
         break
     print(4-atmpt, "attempts left")
     atmpt = atmpt + 1


if atmpt>4:
    print("GAME OVER")





