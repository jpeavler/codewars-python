#Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
def create_phone_number(n):
    result = "("    #start phone number with open parenthesis
    #enumerate allows us to get both the value and index values while looping through the array
    for index, i in enumerate(n):     #loop through array n, i represents value at current index
        result = result + str(i)      #add the next number to the phone number string
        if index == 2:                #If statement to add close parenthesis
            result = result + ") "
        elif index == 5:              #Else if used to add hyphen to phone number string
            result = result + "-"
    return result                     #Once for loop is done, return the result string