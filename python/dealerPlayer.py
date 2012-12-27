import deck as deck
import player as player

class DealerPlayer(player.Player):
	#dealer hits until 17 (some casinos have dealer hit on soft 17, most don't)
	def takeTurn(self):
		handval, ace = self.getHandVal()
		print "dealer taking a turn"
		if handval < 17:
			return ['h', "dealer hit"]
		else:
			return ['p', "dealer pass"]

	def printHand(self):
		return str([self.hand[0]])
