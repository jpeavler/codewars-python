#square_digits takes in a number, squares every digit of that number and returns that number
def square_digits(num):
    digits = [str(int(digit)**2) for digit in str(num)] #makes a list of strings representing the squared value of each digit in the original number
    return int("".join(digits)) #combines all those strings into a number