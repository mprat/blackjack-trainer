import deck as deck
import player as player

class DealerPlayer(player.Player):
	#TODO: implement turn
	def takeTurn(self):
		handval = deck.getHandVal(self.hand)
		print "handval = ", handval
		print "dealer taking a turn"
