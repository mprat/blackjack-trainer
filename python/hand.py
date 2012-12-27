import game
import actions

Start = actions.Action('start')

class PlayerError(Exception):
    pass


class DoubleDownError(PlayerError):
    pass


class SplitError(PlayerError):
    pass


class Hand():
    def __init__(self, cards, bet=0):
        self.cards = cards
        self.bet = bet
        self.double_down = False
        self.history = [Start]

    def append(self, card):
        if self.double_down:
            raise DoubleDownError("Can't hit after double down")
        else:
            self.cards.append(card)

    def split(self):
        """
        Split this hand and return the newly formed hand
        """
        if not game.valid_split(self):
            raise SplitError("Can't split this hand: %s" % self)

        new_hand = Hand([self.cards[1]], self.bet)
        new_hand.history.append(actions.Split)
        self.cards = self.cards[0]
        return new_hand

    def __str__(self):
        return str(self.cards)

    @property
    def value(self):
        handval = sum(game.CARDS[c] for c in self.cards)
        if self.is_soft and handval < 12:
            handval += 10
        return handval

    @property
    def is_blackjack(self):
        return 'A' in self.cards and self.value == 21 and self.history == [Start]

    @property
    def is_bust(self):
        return self.value > 21

    @property
    def is_soft(self):
        return 'A' in self.cards