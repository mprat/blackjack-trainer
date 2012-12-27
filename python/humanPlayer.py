import player as player

class HumanPlayer(player.Player):
	def __init__(self):
		player.Player.__init__(self)
		self.dealerUpCard = []

	def setDealerUpCard(self, card):
		self.dealerUpCard = [card]

	def takeTurn(self):
		print "human taking turn"
		action = raw_input("Action: ")
		print "Entered:", action
		self.checkAction(action)
		return [action, "human taking turn"]

	def checkAction(self, action):
		handval, ace = self.getHandVal()
		handtype = "hard"
		if ace and handval + 10 <= 21:
			handtype = "soft"
			handval = handval + 10
		print "My handval: ", handtype, handval,"and dealer up: ", self.dealerUpCard
