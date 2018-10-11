from baseCreature import BaseCreature

class Mobile(BaseCreature):
    def __init__(self):
        super.__init__(self)
        # a mobile entity that can move room to room
        # with wants and needs.
        self.name = 'unnamed mobile'
        self.attitude = 'neutral'