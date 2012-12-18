from random import shuffle

class Deck:
	def __init__(self, numdecks):
		self.cards = {"2": 4 * numdecks, "3": 4 * numdecks, "4": 4 * numdecks, "5": 4 * numdecks, "6": 4 * numdecks, "7": 4 * numdecks, "8":4 * numdecks, "9": 4 * numdecks, "10": 4 * numdecks, "J": 4 * numdecks, "Q":4 * numdecks, "K":4 * numdecks, "A": 4 * numdecks}

	def getDeckAsDict(self):
		return self.cards

	def getDeckAsList(self):
		cardslist = []
		for (k, v) in self.cards.items():
			for card in range(v):
				cardslist.append(k)
		return cardslist

	def drawCard(self):
		decklist = self.getDeckAsList()
		shuffle(decklist)
		card = decklist.pop()
		self.cards[card] = self.cards[card] - 1
		return card
