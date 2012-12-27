class Player:
	def __init__(self):
		self.hand = []

	def updateHand(self, hand):
		self.hand = hand

	def addCardToHand(self, card):
		self.hand.append(card)

	def printHand(self):
		return str(self.hand)

	def getHandVal(self):
		values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
		handval = 0
		ace = False
		for card in self.hand:
			handval = handval + values[card]
			if card == "A":
				ace = True
		return [handval, ace]
