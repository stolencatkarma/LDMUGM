# combat should start a mininmap type engangement where
# everyone takes turns moving on a grid and using their skills

# maybe a chess board type setup. where the character or team starts on one side
# and the enemies are on the other and combat commences. 

# combat is action oriented where characters and mobiles take turns until one side runs away or is wiped out.

class CombatArena:
    """ created when characters and mobiles enter combat and is assigned to a room. """
    # if room.active_combat_arena then other characters may join in.
    def __init__(self, characters, mobiles):
        """ map is the height map of the combat room. only one character or mobile may be in the same space. """
        self.tiles = list()
        for x in range(8): # 0-7
            for y in range(8): # 64 CombatTile(s)
                self.tiles.append(CombatTile(x, y, 0)) # initalize the map.
        
        # read the room's Combat_arena setup and height_map


class CombatTile:
    def __init__(self, x, y, height):

        self.creature = None # init with None
        self.tile_type = 't_grass'
        self.x = x
        self.y = y
        """ self.height is for the height map """
        self.height = height

    def move_cost(self, creature, from_height):
        if 'FLYING' in creature.tags:
            return int(1)
        else:
            """ move_cost can't be negative. """
            return int(abs(self.height - from_height)) 





