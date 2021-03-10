#Given: an array containing hashes of names
#Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
def namelist(names):
    nameString = ""
    for num, name in enumerate(names):
        if num == 0:    #If it is the first name in the list
            nameString += name['name']    #Just add the name
        elif num == len(names) - 1:    #If it is the final name
            nameString += " & " + name['name']    #include the '&'
        else:    #If it is not the first or last name in the list
            nameString += ", " + name['name']    #add comma and spacing
    return nameString