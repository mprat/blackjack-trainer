from random import shuffle
from deck import *
import dealerPlayer as dealerPlayer 
import humanPlayer as humanPlayer

class Game:
	def __init__(self, deck, numplayers=2):
		self.deck = deck
		self.numplayers = numplayers
		self.discard = Deck(0)
		self.players = {}
		self.players[0] = dealerPlayer.DealerPlayer()
		for p in range(numplayers - 1):
			self.players[int(str(p + 1))] = humanPlayer.HumanPlayer()
		self.lastcommand = "f" #f for first
		self.validcommands = ["h", "dd", "s", "p"]
		self.commandhistory = []

	def startGame(self):
		self.dealRound()
		self.printHandState()
		end = False
		losernum = 0
		while ((not end) and (not self.dealerAndAllPlayersPass())):
			self.commandhistory = []
			self.getCommand(1)
			self.printHandState()
			self.dealerPlay()
			self.printHandState()
			end, losernum = self.checkLoser()
		if end:
			self.endGame(losernum)
		else:
			self.endGame(losernum, "winner")

	def dealerAndAllPlayersPass(self):
		if len(self.commandhistory) < 1:
			return False
		else:
			for command in self.commandhistory:
				if not command == "p":
					return False
			return True

	def dealerPlay(self):
		action, message = self.players[0].takeTurn()
		#print message
		self.processAction(action, 0)

	#TODO: implement end of game
	def endGame(self, playernum, msg = "loser"):
		print "The game is over. Player " + str(playernum) + " is the " + msg + "."
		print "Dealer score: ", self.players[0].getHandVal()
		print "Player 1 score: ", self.players[1].getHandVal()
		#TODO: clear the field, add cards to discard	
		#self.startGame

	def checkLoser(self):
		highestHandVal = 0
		winningplayer = 0
		for playernum, player in self.players.iteritems():
			handval, ace = player.getHandVal()
			if handval > highestHandVal:
				highestHandVal = handval
				winningplayer = playernum
			if handval > 21:
				return [True, playernum]
		return [False, winningplayer]

	def getCommand(self, playernum):
		action = raw_input("Action: ")
		print "Entered:", action
		self.processAction(action, playernum)	

	def processAction(self, action, playernum):
		if action in self.validcommands:
			if action == "h":
				self.playerHit(playernum)
			elif action == "dd":
				self.playerDD(playernum)
			elif action == "s":
				self.playerSplit(playernum)
			elif action == "p":
				print "PASS"
				#HACK. only works with two players
				#if self.lastcommand == "p":
				#	end, winner = self.checkLoser()
				#	self.endGame(winner, "winner")
			self.lastcommand = action
			self.commandhistory.append(action)
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