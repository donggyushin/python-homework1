# Make a program that matches what kind of student you are with using confitional statements.
# The conditions this program has are below.

# Calculate ages as 2020 - the year you were borned + 1
# lower than 26 and upper than 20, college student
# lower than 20 and upper than 17, high school student
# lower than 17 and upper than 14, middle school student
# lower than 14 and upper than 8, elementary shcool student
# else, print 'you are not a student. '

# function that calculates age from the year user entered


def calculateAge(year):
    return 2020 - year + 1


def main():

    print('Input when you were borend')
    year = int(input())
    age = calculateAge(year)
    if age <= 26 and age >= 20:
        print('you are a college student')
    elif age < 20 and age >= 17:
        print('you are a high school student')
    elif age < 17 and age >= 14:
        print('you are a middle school student')
    elif age < 14 and age >= 8:
        print('you are a elementary school student')
    else:
        print('you are not a student')


if __name__ == '__main__':
    main()
