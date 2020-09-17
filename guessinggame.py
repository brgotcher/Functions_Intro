import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("Please enter a valid integer")


highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: remove after testing

guess = 0
print("Please guess number between 1 and {}: ".format(highest))
while guess != answer:
    guess = get_integer(": ")
    if guess == 0:
        print("quitter!")
        break
    elif guess == answer:
        print("Correct!")
        break
    else:
        if guess < answer:
            print("Please guess higher or enter '0' to quit")
        else:   # guess must be greater than answer
            print("Please guess lower or enter '0' to quit")

