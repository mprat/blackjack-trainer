import deck
import dealerPlayer
import humanPlayer
import actions

CARDS = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

HIT_ON_SOFT_17 = False


def valid_split(hand):
    return len(hand.cards) == 2 and CARDS[hand.cards[0]] == CARDS[hand.cards[1]]


class Game:
    def __init__(self, numplayers=2, numdecks=1):
        self.deck = deck.Deck(numdecks=numdecks)
        self.numplayers = numplayers
        self.dealer = dealerPlayer.DealerPlayer(0)
        self.humans = [humanPlayer.HumanPlayer(p + 1) for p in range(numplayers - 1)]
        self.players = [self.dealer] + self.humans

    def startGame(self):
        self.dealRound()
        self.printHandState()
        while not self.allPlayersPass():
            for player in self.humans:
                self.takeTurn(player)
            if all(h.is_bust for p in self.humans for h in p.hands):
                self.endGame()
        print "Humans finished"
        while not self.dealer.last_actions[0] == actions.Pass:
            self.takeTurn(self.dealer)
            if self.dealer.hands[0].is_bust:
                break
        self.endGame()

    def takeTurn(self, player):
        for hand, action in player.takeTurn():
            self.processAction(action, player, hand)

    def processAction(self, action, player, hand):
        print "Player", player.player_num, "hand", hand, "action", action
        if action == actions.Hit:
            player.hit(hand, self.deck.drawCard())
        elif action == actions.Pass:
            pass
        elif action == actions.DoubleDown:
            player.doubleDown(hand, self.deck.drawCard())
        elif action == actions.Split:
            player.split(hand, self.deck.drawCards(2))

    def allPlayersPass(self):
        return all(action == actions.Pass for p in self.humans for action in p.last_actions)

    def endGame(self):
        for player in self.players:
            print "Player", player.player_num
            for hand in player.hands:
                print "Hand", hand, "score:", hand.value

    def dealRound(self):
        for player in self.players:
            cards = self.deck.drawCards(player.num_hands * 2)
            player.deal_hands(cards)

    def printHandState(self):
        for player in self.players:
            print "Player", player.player_num, ":", player.handStr()
