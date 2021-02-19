def to_jaden_case(string):
    stringListCapped = [word.capitalize() for word in string.split()]    #split string into list and capitalize each word
    separator = " "    #Used by join function to add spaces between list items
    return separator.join(stringListCapped)    #rejoin list into string separated by spaces