from random import shuffle
from deck import *
import dealerPlayer as dealerPlayer 
import humanPlayer as humanPlayer

class Game:
	def __init__(self, deck, numplayers=2):
		self.deck = deck
		self.numplayers = numplayers
		self.discard = Deck(0)
		#self.playerhands = {}	
		#for p in range(numplayers): #0 is the dealer hand
		#	self.playerhands[str(p)] = []
		self.players = {}
		self.players[0] = dealerPlayer.DealerPlayer()
		for p in range(numplayers - 1):
			self.players[int(str(p + 1))] = humanPlayer.HumanPlayer()

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
		self.players[0].takeTurn()

	#TODO: implement end of game
	def endGame(self, losernum):
		print "The game is over. Player " + str(losernum) + " is the loser."

	def checkLoser(self):
		for playernum, player in self.players.iteritems():
			handval, ace = player.getHandVal()
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
		player = self.players[playernum]
		card = self.deck.drawCard()
		player.addCardToHand(card)

	#TODO: implement player double down
	def playerDD(self, playernum):
		print "DOUBLE DOWN"

	#TODO: implement player split
	def playerSplit(self, playernum):
		print "SPLIT"
	
	def dealRound(self):
		for playernum, player in self.players.iteritems():
			card = self.deck.drawCard()
			player.addCardToHand(card)
			card2 = self.deck.drawCard()
			player.addCardToHand(card2)

	def printHandState(self):
		for playernum, player in self.players.iteritems():
			print "Player",playernum,":", player.printHand()