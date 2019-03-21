# Make multiplication table calculator with using for in this Lab.
# The rules of multiplication table calculator are same as below.

# Print 'Which level of multiplication table do you want?' after start program
# User enters number of level of multiplication table that user wants to calculate.
# Program prints the result of multiplication table with message 'Calculate n-th multiplication table..'


def calculateMultiplication(number):
    print('Calculate ', number, '-th multiplication table')
    for item in range(1, 10):
        print("{} x {} = {}" .format(number, item, number*item))


def main():
    print('Which level of multiplication table do you want?')
    levelOfMultiplication = int(input())
    calculateMultiplication(levelOfMultiplication)


if __name__ == '__main__':
    main()
