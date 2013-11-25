#Evan Hopkins
#Runaway Bot
#v1.01
import rg
import random

class Robot:
    def act(self, game):
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]

        newLoc = randomLocation(self.location)
        return ['move', rg.toward(newLoc)]

    def randomLocation(self, location):
    	x = random.randint(-1,1)
    	y = random.randint(-1,1)

    	x = x + location[0]
    	y = y + location[1]

    	if (x==y):
    		newLoc = randomLocation(location)
    	else:
    		newLoc = (x,y)
    	return newLoc