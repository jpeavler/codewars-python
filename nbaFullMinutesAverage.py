#defining nba_extrap to take in a player's scored points per game and
#the number of minutes per game. Returns a float representing the number
#of points a player would score if they played the full game.
def nba_extrap(ppg, mpg):
    if(mpg == 0):    #avoid dividing by zero
        return 0
    return round(ppg * 48 / mpg, 1)    #divide by the minutes they played and multiply
#the full game length