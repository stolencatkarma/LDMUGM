from calendar import Calendar

class Plane: # Plane of existance
    def __init__(self, name):
        # load file /planes/name.plane
        # players dont care about this unless
        # using a planar exit.
        self.name = name
        self.owners = list() # list of characters who can act as admins
        self.calendar = Calendar(0, 0, 0, 0, 0, 0)
        self.rooms = list()
        self.room_map = dict()
        # i want a map that shows connected rooms
        # in a 3d view by room coordinates
        # connect by lines showing exits

        def parse_rooms(self):
            for room in self.rooms:
                # parse x,y,z
                # parse exits and planar exits
                pass
        