# Make a continuous multiplication table calculator program with using for and
# conditional statement we have learned
# The rules of program are same as below.

# print message 'Which level of multiplication table do you want to start?' after start.
# User enters the number user wants to play
# Program prints result of multiplication table with message 'calculate n-th multiplication table'
# This program is different with previous example,
# If user enters 0, then program should be ended. But user didn't enter 0, then program
# will not be ended.


def multiplicationTable(number):
    print('calculate {}-th multiplication table'.format(number))
    # Make a loop that repeat from 1 to 9
    for i in range(10):
        print('{} x {} = {}'.format(number, i, number * i))


def main():
    levelOfMultiplication = int(1)
    # Make a loop being continuos until levelOfMultiplication becomes 0
    while levelOfMultiplication is not 0:
        print('which level of multiplication table do you want?(1~9)?')
        levelOfMultiplication = int(input())
        # Break loop when levelOfMultiplication becomes 0
        if levelOfMultiplication is 0:
            break
        multiplicationTable(levelOfMultiplication)
    print('Quit program')
    return


if __name__ == '__main__':
    main()
