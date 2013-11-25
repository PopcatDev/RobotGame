import rg
import random

class Robot:
	#Runaway Bot
    def act(self, game):
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]

        newLoc = randomLocation()
        return ['move', rg.toward(newLoc)]

    def randomLocation(self):
    	x = random.randint(-1,1)
    	y = random.randint(-1,1)
    	if (x==y):
    		newLoc randomLocation()
    	else:
    		newLoc = (x,y)
    	return newLoc