class Exit:
    def __init__(self, command, exit_id, desc, planar=False):
        # a planar exit leads to another plane of existance. 
        # we dont want to map rooms on different Planes for Plane
        self.command = str(command)
        self.exit_id = int(exit_id)
        self.hidden = None # MAGICAL, REGULAR
        self.desc = str(desc) # max width 80

    def __eq__(self, other):
        if(self.command == other.command and self.exit_id == other.exit_id and self.desc == other.desc):
            return True
        return False

    def __hash__(self):
        return hash(self.command + self.exit_id + self.desc)