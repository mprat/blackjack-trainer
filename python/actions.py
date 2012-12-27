

class Action(object):
    def __init__(self, desc):
        self.desc = desc

    def __str__(self):
        return str(self.desc)

Hit = Action('hit')
Pass = Action('pass')
Split = Action('split')
DoubleDown = Action('double down')

lookup = {'h': Hit, 'p': Pass, 's': Split, 'dd': DoubleDown}
