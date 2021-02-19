#positive_sum takes a list of numbers and finds the sum of the positive numbers in that list
def positive_sum(numberList):
    positiveSum = 0
    for number in numberList:
        if number > 0:
            positiveSum += number
    return positiveSum