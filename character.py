from baseCreature import BaseCreature

# the object connecting players control within the game world.
# stored in files under the folder name for logins
class Character(BaseCreature):
    def __init__(self):
        super.__init__(self)
        self.first = 'John'
        self.last = 'Doe'
        self.plane = 'tutorial'
        self.room_id = 1 # the room the Character is in.
        self.parts = list() # body parts

        """ Teams are groups of 2-64 players who move and fight together. """
        self.team = None
        """ This character is dead if True. They may be brought back to life though. """
        self.dead = False
    
    def full_name(self):
        return str(self.first, self.last)

