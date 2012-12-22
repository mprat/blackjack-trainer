from random import shuffle
from deck import *
import dealerPlayer as dealerPlayer 

class Game:
	def __init__(self, deck, numplayers=2):
		self.deck = deck
		self.numplayers = numplayers
		self.discard = Deck(0)
		self.playerhands = {}	
		for p in range(numplayers): #0 is the dealer hand
			self.playerhands[str(p)] = []
		

	def startGame(self):
		self.dealRound()
		self.printHandState()
		self.getCommand(1)
		self.printHandState()
		self.dealerPlay()
		self.printHandState()
		end, losernum = self.checkLoser()
		while (not end):
			self.getCommand(1)
			self.printHandState()
			end, losernum = self.checkLoser()
		self.endGame(losernum)

	#TODO: implement dealer play
	def dealerPlay(self):
		print "dealer play"

	#TODO: implement end of game
	def endGame(self, losernum):
		print "The game is over. Player " + str(losernum) + " is the loser."

	#TODO: implement loss-checking state
	def checkLoser(self):
		for playernum, hand in self.playerhands.items():
			handval, ace = self.deck.getHandVal(hand)
			if handval > 21:
				return [True, playernum]
		return [False, 0]

	def getCommand(self, playernum):
		action = raw_input("Action: ")
		print "Entered:", action
		self.processAction(action, playernum)	

	def processAction(self, action, playernum):
		if action == "h":
			self.playerHit(playernum)
		elif action == "dd":
			self.playerDD(playernum)
		elif action == "s":
			self.playerSplit(playernum)
		elif action == "p":
			print "PASS"
		else:
			print "Invalid command. Valid commands: h, dd, s, p"
			self.getCommand(playernum)

	def playerHit(self, playernum):
		print "HIT"
		card = self.deck.drawCard()
		self.playerhands[str(playernum)].append(card)

	#TODO: implement player double down
	def playerDD(self, playernum):
		print "DOUBLE DOWN"

	#TODO: implement player split
	def playerSplit(self, playernum):
		print "SPLIT"
	
	def dealRound(self):
		#print self.deck
		#print self.playerhands
		for p in 2*range(self.numplayers):
			card = self.deck.drawCard()
			self.playerhands[str(p % self.numplayers)].append(card)

	def printHandState(self):
		toprint = []
		for (k, v) in self.playerhands.items():
			if k == '0': 
				toprint.append((k, v[0]))
			elif k == '1':
				toprint.append((k, v))
		print toprint	
