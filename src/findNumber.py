# Make a program that finds specific number with using for and conditional statement.
# The rules of this program are same as below.

# At first, computer generates random number between 1 and 100.
# Then, computer compares the number user entered and the number computer generated.
# Print 'Correct' when user entered correct number.
import random


def compareNumbers(computerNumber, userNumber):
    if computerNumber > userNumber:
        return 1
    elif computerNumber < userNumber:
        return -1
    else:
        return 0


def generateRandomNumber():
    return int(random.randrange(1, 101))


def main():
    computerNumber = generateRandomNumber()
    print('Enter any number between 1 and 100')
    userNumber = int(input())
    result = compareNumbers(computerNumber, userNumber)
    if result is 0:
        print('Correct!')
        return
    else:
        while not(result is 0):
            if result is -1:
                print('Too big')
                print('Enter lower number')
            else:
                print('Too small')
                print('Enter upper number')
            userNumber = int(input())
            result = compareNumbers(computerNumber, userNumber)

        print('Correct!')
        return


if __name__ == '__main__':
    main()
