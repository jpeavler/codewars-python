#count_sheeps takes in a list of booleans (True values representing sheep present) and returns the number of True
def count_sheeps(sheeps):
    count = 0
    for sheep in sheeps:
        if sheep:
            count += 1
    return count