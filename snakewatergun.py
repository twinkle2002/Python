import random
# random_number = random.randint(0,2)
# print(random_number)
list = ["water", "gun","snake"]
# choice = random.choice(list)
# print("computer's choice")
# print(choice)


print("s for snake")
print("w for water")
print("g for gun")

coputer_point = 0
human_point = 0
attempts = 10
no_of_attempts = 0
while no_of_attempts<attempts:

    choice = random.choice(list)
    print("computer's choice")
    print(choice)
    i = input("enter your choice \n")

    if i==choice:
        print("Tie \n")

    elif input=="s" and choice=="w":
        print(f"your guess {input} and computer's choice is {choice} \n")
        print("you won")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif input=="g" and choice=="w":
        print(f"your guess {input} and computer's choice is {choice} \n")
        print("you loose")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif input=="s" and choice=="g":
        computer_point = computer_point + 1
        print(f"your guess {input} and computer's choice is {choice} \n")
        print("you loose")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif input=="g" and choice=="s":
        print(f"your guess {input} and computer's choice is {choice} \n")
        print("you won")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif input=="w" and choice=="g":
        print(f"your guess {input} and computer's choice is {choice} \n")
        print("you won")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif input=="s" and choice=="g":
        print(f"your guess {input} and computer's choice is {choice} \n")
        print("you loose")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    else:
        print("wrong input")

    no_of_attempts==no_of_attempts + 1
    print(f"{attempts - no_of_attempts} is left")



print("over")

if computer_point==human_point:
    print("Tie")

elif computer_point>human_point:
    print("Computer wins")

else:
    print("You win")

print(f" your point is {human_point} and computer point is {computer_point}")