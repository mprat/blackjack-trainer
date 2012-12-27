import random
import game
random.seed(1)


class DeckEmptyException(Exception):
    pass


class Deck:
    def __init__(self, numdecks=1):
        self.cards = [c for i in range(4 * numdecks) for c in game.CARDS]
        self._card_index = 0
        self.shuffle()

    def drawCard(self):
        if self._card_index < len(self.cards):
            self._card_index += 1
            return self.cards[self._card_index - 1]
        else:
            print "Shuffling deck"
            self.shuffle()
            self._card_index = 0
            return self.drawCard()

    def drawCards(self, num):
        for i in range(num):
            yield self.drawCard()

    def shuffle(self):
        random.shuffle(self.cards)
