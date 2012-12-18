from random import shuffle
from deck import *

class Game:
	def __init__(self, deck, numplayers):
		self.deck = deck.getDeckAsList()
		self.players = numplayers
		self.discard = {}
		self.playerhands = {}	
		shuffle(self.deck)

	def startGame(self):
		self.dealRound()
		
	def dealRound(self):
		print self.deck
