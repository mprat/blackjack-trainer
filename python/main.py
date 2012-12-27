from deck import *
import sys
from game import *

if __name__ == '__main__':
#	if (len(sys.argv) != 2):
#		sys.exit(0)
#	else:
#		deck = Deck(int(sys.argv[1]))
	deck = Deck(1)
	game = Game(deck)
	game.startGame()
		
