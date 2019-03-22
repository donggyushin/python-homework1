# Make continuous average program with using for, conditional statement

# student   A   B   C   D   E
# kor      49   80 20  100  80
# math     43   60 85   30  90
# eng      49   82 48   50  100

# The rules of this program are same as below
# Call every row and add every column value of each row then calculate average of total score
# Use 2 for


def getAverageScore(studentsScore):
    totalScore = [0, 0, 0, 0, 0]
    i = 0
    # 'for' statement for getting total score
    for row in studentsScore:
        for column in row:
            totalScore[i] = totalScore[i]+column
            i = i+1
        i = 0
    # Get length of studentsScore to get average of the totalscore
    length = len(studentsScore)
    for item in totalScore:
        # Get average value by dividing total score by length
        totalScore[i] = item / length
        i = i+1
    averageScore = totalScore
    return averageScore


def main():
    kor = [49, 80, 20, 100, 80]
    math = [43, 60, 85, 30, 90]
    eng = [49, 82, 48, 50, 100]
    # Tie every score group to one group to make it easy to calculate
    studentsScore = [kor, math, eng]
    averageScore = getAverageScore(studentsScore)
    print('Average score is {}'.format(averageScore))


if __name__ == '__main__':
    main()
