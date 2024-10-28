import random


def randomNumberFunction():
    randomNumber = random.randint(1,10)

    inputNumber = int(input('Please enter a random number between 1 and 10:'))

    if randomNumber == inputNumber:
        print('Your number matches')
    if inputNumber > randomNumber:
        print('Your number is too high, guess again')
        randomNumberFunction()
    if inputNumber < randomNumber:
        print("Your number is too low, guess again")
        randomNumberFunction()

randomNumberFunction()

