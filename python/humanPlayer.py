import player
import actions


class HumanPlayer(player.Player):
    def getAction(self, hand):
        print "Current hand:", hand
        while True:
            action = raw_input("Action: ")
            if self.checkAction(action):
                break
            else:
                print "I didn't understand this action: %s" % action
        return actions.lookup[action]
