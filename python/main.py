from deck import *
import sys
from game import *

if __name__ == '__main__':
	if (len(sys.argv) != 3):
		sys.exit(0)
	else:
		deck = Deck(int(sys.argv[1]))
		numplayers = int(sys.argv[2])
		game = Game(deck, numplayers)
		game.startGame()
		
