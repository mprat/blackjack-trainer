import actions
import hand


class Player(object):
    def __init__(self, player_num, deck, num_hands=1, money=100, bet=1):
        self.deck = deck
        self.hands = []
        self.num_hands = num_hands
        self.money = money
        self.bet = bet
        self.player_num = player_num

    @property
    def action_history(self):
        return [h.history for h in self.hands]

    @property
    def last_actions(self):
        return [hist[-1] for hist in self.action_history]

    def deal_hands(self, cards):
        cards = list(cards)
        assert len(cards) == 2 * self.num_hands
        self.hands = [hand.Hand([cards.pop(), cards.pop()], bet=self.bet) for i in range(self.num_hands)]

    def takeTurn(self):
        for hand in self.hands:
            while hand.last_action != actions.Pass:
                if hand.is_bust or hand.double_down:
                    action = actions.Pass
                else:
                    action = self.getAction(hand)
                hand.history.append(action)
                self.processAction(action, hand)

    def processAction(self, action, hand):
        print "Performing action:", action
        if action == actions.Hit:
            self.hit(hand)
        elif action == actions.Pass:
            pass
        elif action == actions.DoubleDown:
            self.doubleDown(hand)
        elif action == actions.Split:
            self.split(hand)
        print "Hand after action:", hand

    def getAction(self):
        """
        Abstract
        """
        raise NotImplementedError

    def handStr(self):
        return [str(h) for h in self.hands]

    def checkAction(self, action):
        """
        returns True for valid action
        """
        return action in actions.lookup

    def hit(self, hand):
        card = self.deck.drawCard()
        hand.cards.append(card)

    def doubleDown(self, hand):
        card = self.deck.drawCard()
        hand.cards.append(card)
        hand.double_down = True
        hand.bet *= 2

    def split(self, hand):
        cards = list(self.deck.drawCards(2))
        self.hands.append(hand.split())
        hand.cards.append(cards[0])
        self.hands[-1].cards.append(cards[1])
