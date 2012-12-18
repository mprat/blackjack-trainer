from random import shuffle
from deck import *

class Game:
	def __init__(self, deck, numplayers=1):
		self.deck = deck
		self.numplayers = numplayers
		self.discard = Deck(0)
		self.playerhands = {}	
		for p in range(numplayers): #0 is the dealer hand
			self.playerhands[str(p)] = []

	def startGame(self):
		self.dealRound()
		self.getCommand()
		self.dealerPlay()
		end = self.checkLoser()
		while (not end):
			self.getCommand()
			end = self.checkLoser()
		self.endGame()

	#TODO: implement dealer play
	def dealerPlay(self):
		print "dealer play"

	#TODO: implement end of game
	def endGame(self):
		print "The game is over"

	#TODO: implement loss-checking state
	def checkLoser(self):
		for playernum, hand in self.playerhands.items():
			print (playernum, hand)
		return False

	def getCommand(self):
		action = raw_input("Action: ")
		print "Entered:", action
		self.processAction(action)	

	#TODO: implement actions
	def processAction(self, action):
		if action == "h":
			self.playerHit()
		elif action == "dd":
			self.playerDD()
		elif action == "s":
			self.playerSplit()
		elif action == "p":
			print "PASS"
		else:
			print "Invalid command. Valid commands: h, dd, s, p"
			self.getCommand()

	#TODO: implement player hit
	def playerHit(self):
		print "HIT"

	#TODO: implement player double down
	def playerDD(self):
		print "DOUBLE DOWN"

	#TODO: implement player split
	def playerSplit(self):
		print "SPLIT"
	
	def dealRound(self):
		#print self.deck
		#print self.playerhands
		for p in 2*range(self.numplayers):
			card = self.deck.drawCard()
			self.playerhands[str(p % self.numplayers)].append(card)
		self.printHandState()

	def printHandState(self):
		toprint = []
		for (k, v) in self.playerhands.items():
			if k == '0': 
				toprint.append((k, v[0]))
			elif k == '1':
				toprint.append((k, v))
		print toprint	
