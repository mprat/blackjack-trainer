from random import shuffle
from deck import *

class Game:
	def __init__(self, deck, numplayers):
		self.deck = deck
		self.numplayers = numplayers
		self.discard = Deck(0)
		self.playerhands = {}	
		for p in range(numplayers): #0 is the dealer hand
			self.playerhands[str(p)] = []

	def startGame(self):
		self.dealRound()
		
	def dealRound(self):
		#print self.deck
		#print self.playerhands
		for p in 2*range(self.numplayers):
			card = self.deck.drawCard()
			self.playerhands[str(p % self.numplayers)].append(card)

		print self.playerhands
