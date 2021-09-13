

def next_palindrome(n):
    n = n + 1
    while not is_palindrome(n):
        n += 1
    return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    size = int(input("Enter the size of your list \n"))
    numbers = []

    for i in range(size):
        numbers.append(int(input("Enter the number of the list \n")))
        print(f"You have entered the list {numbers} \n")

new_list = []
for element in numbers:
    if element > 10:
        n = next_palindrome(element)
        new_list.append(n)

    else:
        new_list.append(element)

print(f"Output list is {new_list}")