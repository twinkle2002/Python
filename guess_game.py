import random

def guessGame(a, b, random_number):
    guess = int(input(f"Enter the number between {a} and {b} \n"))
    nguess = 1
    while guess != random_number:
        if guess < random_number:
            guess = int(input("go towards large number \n"))
            nguess += 1

        else:
            guess = int(input("go towards small number \n"))
            nguess += 1


    print(f"You guess the number in {nguess} guesses \n")
    return nguess

if __name__ == '__main__':

    a = int(input("Enter the value of a \n"))
    b = int(input("Enter the value of b \n"))
    random_number1 = random.randint(a,b)
    print("Player-1's turn")
    g1 = guessGame(a, b, random_number1)
    random_number2 = random.randint(a, b)
    print("Player-2's turn")
    g2 = guessGame(a, b, random_number2)

    if g2 > g1:
        print("Player-1 wins \n")

    if g2 < g1:
        print("Player-2 wins \n")

    else:
        print("It's a Tie !!! \n")

print(f"Random number for player-1 is {random_number1} and player-2 is {random_number2}")









