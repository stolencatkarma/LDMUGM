from character import Character

class NonPlayer(Character):
    # special type of character with their
    # own sets of goals. May join players.
    # server WILL process these as if they 
    # were a active connected player.
    def __init__(self):
        super.__init__(self)
        self.personality = 'neutral'