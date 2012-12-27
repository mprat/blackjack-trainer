import actions
import hand


class Player(object):
    def __init__(self, player_num, num_hands=1):
        self.hands = []
        self.num_hands = num_hands
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
        self.hands = [hand.Hand([cards.pop(), cards.pop()]) for i in range(self.num_hands)]

    def takeTurn(self):
        result = []
        for hand in self.hands:
            if hand.is_bust or hand.double_down:
                action = actions.Pass
            else:
                action = self.getAction(hand)
                hand.history.append(action)
                result.append((hand, action))
        return result

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

    def hit(self, hand, card):
        hand.cards.append(card)

    def doubleDown(self, hand, card):
        hand.cards.append(card)
        hand.double_down = True

    def split(self, hand, cards):
        cards = list(cards)
        self.hands.append(hand.split())
        hand.cards.append(cards[0])
        self.hands[-1].cards.append(cards[1])
