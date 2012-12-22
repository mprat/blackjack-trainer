import deck as deck

class DealerPlayer:
	def __init__(self, hand):
		self.hand = hand
	
	#TODO: implement turn
	def takeTurn(self):
		handval = deck.getHandVal(self.hand)
		print "handval = ", handval
		print "dealer taking a turn"
