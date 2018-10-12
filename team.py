class Team:
    """ Characters and NonPlayersCharacters can join this. """
    def __init__(self, leader, name):
        self.leader = leader
        self.name = name

        """ the list of team mates. includes leader. """
        self.mates = list() 

    def change_leader(self, character):
        self.leader = character