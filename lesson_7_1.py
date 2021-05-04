import random

random_number = random.randrange(50)
# print(random_number)

attempts = 7

while attempts > 0:
    print("Attempts left:" + str(attempts))
    attempts -= 1
    guessed_number = int(input("Guess the number?"))
    if guessed_number == random_number:
        print("You guessed correctly")
        attempts = 0
    elif guessed_number < random_number:
        print("The number you gave is too low")
    else:
        print("The number you gave is too high")


