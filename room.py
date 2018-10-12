class Room:
    def __init__(self, unique_id):
        # size? how far away from each other things can be
        self.unique_id = unique_id
        self.title = 'room title'
        self.desc = 'long room description'
        self.ascii_art = '' # if you want a ascii art pic shown
        self.mobiles = list()
        self.items = list()
        self.exits = list() # list of Exit()
        self.icon = 'o' # for world map
        self.tags = list() # ['DEADLY', 'NO_COMBAT']
        self.x = 0
        self.y = 0
        self.z = 0
        """ combat_arena is where creatures and mobiles in this room do combat in a turn based fashion. """
        self.combat_arena = None 
        
    def on_enter(self, object): pass
    def on_exit(self, object): pass
    
        
    def __eq__(self, other):
        if(self.unique_id == other.unique_id):
            return True
        return False
    
    def __hash__(self):
        return hash(self.unique_id)