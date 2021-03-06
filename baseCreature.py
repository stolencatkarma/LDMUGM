class BaseCreature:
    def __init__(self):
        """ factions will be stored by name and able to be custom. """
        self.faction = None
        self.name = 'unnamed BaseCreature'
        self.size = float(1) # 1.0 is human sized. for ranged combat
        self.parts = list() # body parts
        self.stats = dict()
        self.skills = list() # most creatures can 'move'
        self.race = 'unset Race'
        # inventory is handled by body part equipped 
        # containers 
        self.path = list() # for pathfinding
        self.tags = list() # ['FLYING', 'BLESSED', 'ETC...']

    def use_skill(self, skill, target=None, room=None):
        # use a skill if it exists in skills.
        pass