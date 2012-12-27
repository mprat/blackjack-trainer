import player
import actions
import game


class DealerPlayer(player.Player):
    def getAction(self, hand):
        handval = hand.value
        if handval < 17:
            return actions.Hit
        elif handval == 17 and hand.is_soft and game.HIT_ON_SOFT_17:
            return actions.Hit
        else:
            return actions.Pass

    def handStr(self):
        return self.getUpCard()

    def getUpCard(self):
        assert len(self.hands) == 1, "Dealer should only have one hand"
        return self.hands[0].cards[0]
