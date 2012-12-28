import deck
import dealerPlayer
import humanPlayer
import actions

CARDS = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

HIT_ON_SOFT_17 = False

PAYOUTS = {"player_win": 1,
           "dealer_win": 1,
           "player_blackjack": 1.5,
           "dealer_blackjack": 1.5}


def valid_split(hand):
    return len(hand.cards) == 2 and CARDS[hand.cards[0]] == CARDS[hand.cards[1]]


class Game:
    def __init__(self, numplayers=2, numdecks=1):
        self.deck = deck.Deck(numdecks=numdecks)
        self.numplayers = numplayers
        self.dealer = dealerPlayer.DealerPlayer(0, self.deck)
        self.humans = [humanPlayer.HumanPlayer(p + 1, self.deck) for p in range(numplayers - 1)]
        self.players = [self.dealer] + self.humans

    def playGame(self):
        while True:
            print "===== New Round ====="
            self.takeBets()
            self.startRound()
            self.playRound()
            self.endRound()

    def startRound(self):
        self.dealRound()
        self.printHandState()

    def takeBets(self):
        print "Now placing bets"
        for player in self.humans:
            print "------"
            print "Player", player.player_num
            print "Money:", player.money
            print "Current bet per hand:", player.bet
            while True:
                new_bet = raw_input("New bet (blank to keep value, integers only): ")
                if new_bet.strip() != "":
                    new_bet = int(new_bet)
                else:
                    break
                if new_bet * player.num_hands > player.money:
                    print "Not enough money to bet %d per hand for %d hands" % (new_bet, player.num_hands)
                else:
                    player.bet = new_bet
                    break

    def playRound(self):
        while not self.allPlayersPass():
            for player in self.humans:
                player.takeTurn()
            if all(h.is_bust for p in self.humans for h in p.hands):
                return
        print "Humans finished"
        while not self.dealer.last_actions[0] == actions.Pass:
            self.dealer.takeTurn()
            if self.dealer.hand.is_bust:
                break
        return

    def allPlayersPass(self):
        return all(action == actions.Pass for p in self.humans for action in p.last_actions)

    def endRound(self):
        print "Dealer hand:", self.dealer.hand, "value:", self.dealer.hand.value
        for player in self.humans:
            print "Player", player.player_num
            for hand in player.hands:
                print "Hand", hand, "value:", hand.value
                if hand.is_blackjack and not self.dealer.hand.is_blackjack:
                    print "Win (blackjack). Bet:", hand.bet
                    player.money += hand.bet * PAYOUTS['player_blackjack']
                elif self.dealer.hand.is_blackjack and not hand.is_blackjack:
                    print "Lose (dealer blackjack). Bet:", hand.bet
                    player.money -= hand.bet * PAYOUTS['dealer_blackjack']
                elif hand.is_bust:
                    print "Lose (bust). Bet:", hand.bet
                    player.money -= hand.bet * PAYOUTS['dealer_win']
                elif self.dealer.hand.is_bust:
                    print "Win (dealer bust). Bet:", hand.bet
                    player.money += hand.bet * PAYOUTS['player_win']
                elif (hand.value > self.dealer.hand.value):
                    print "Win. Bet:", hand.bet
                    player.money += hand.bet * PAYOUTS['player_win']
                elif hand.value == self.dealer.hand.value:
                    print "Push. Bet:", hand.bet
                else:
                    print "Lose. Bet:", hand.bet
                    player.money -= hand.bet * PAYOUTS['dealer_win']

    def dealRound(self):
        for player in self.players:
            cards = self.deck.drawCards(player.num_hands * 2)
            player.deal_hands(cards)

    def printHandState(self):
        for player in self.players:
            print "------"
            print "Player", player.player_num
            if player.player_num != 0:
                print "Money:", player.money
            print "Hands:", player.handStr()
