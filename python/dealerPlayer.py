import deck as deck
import player as player

class DealerPlayer(player.Player):
	#TODO: implement turn
	#dealer hits until 17 (some casinos have dealer hit on soft 17, most don't)
	def takeTurn(self):
		handval = self.getHandVal()
		print "handval = ", handval
		print "dealer taking a turn"

	def printHand(self):
		return str([self.hand[0]])
