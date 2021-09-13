'''
Author: Twinkle
Date:30th august 2021
Purpose: practice problem
'''
def next_palindrome(n):
    n = n + 1
    while not is_palindrome(n):
        n += 1
    return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':

    n = int(input("Enter the number of test cases \n"))
    numbers = []

    for i in range(n):
        num = int(input("Enter the number \n"))
        numbers.append(num)
    print(numbers)

    for i in range(n):
        print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])} \n")