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
        self.faction = None
        self.profession = 'survivor'
        self.team = None # teams move together
    
    def full_name(self):
        return str(self.first, self.last)