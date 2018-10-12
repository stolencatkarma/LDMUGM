import time
from calendar import Calendar

from action import Action
from command import Command
from exit import Exit
from Mastermind._mm_server import MastermindServerTCP
from plane import Plane
from room import Room
from baseItem import BaseItem
from character import Character
from baseCreature import BaseCreature


class Connection: # a player's connection for logging in
    def __init__(self, account_name, address):
        self.address = address # store the address each time so we can send data to clients with 
                               # server.callback_client_send( server._mm_connections[address], data )
        self.characters = list() # the Characters associated with the account.
        self.action_queue = list() # the list of the actions the character wants to do.
        for character in account_name.file:
            self.characters.append(character)
        self.character = None # after we load a character for the player make a reference of it here.
    
    def load_character(self, character):
        self.character = character


class Server(MastermindServerTCP):
    def __init__(self):
        MastermindServerTCP.__init__(self, 0.5, 0.5, 300.0)
        self.connected_characters = list()
        self.planes = dict() # Planes of existance. by str() name loaded from name.plane in /planes/ so they can be exchanged easily.
        # self.planes['tutorial'].rooms[]
        # 
        # load the list of planes from files
        #

    def compute_turn(self):
        # gather a list of rooms using connected players
        # for each room
            # SORT turn order by speed in BaseCreatures[]
            # for each BaseCreature check their action_queue
                # parse 1 action or turns_until_can_act_again--
                # send message to room of results. (no need to resend room until
                # something moves or dies or gets picked up)
            # tick calendar for this plane.
            # weather? etc?
        pass

    def send_updated_room(self, plane, room):
        """ send all characters on plane and in room an updated room. """
        pass

    def send_message_to_room(self, plane, room, message):
        """ Used to send a message to all characters in a room to their message_window for combat and feedback """
        pass

    def move_object(self, object, plane, from_room, to_room):
        """ move and object from one room to another within the same plane """
        # depending on the class type being moved
        # pick the right list to to and from.
        if isinstance(object, BaseItem):
            pass
        elif isinstance(object, Character):
            # character move differently
            pass
        elif isinstance(object, BaseCreature):
            pass

    def create_room(self, plane, x, y, z):
        pass
    
    def create_plane(self, name):
        """ creates a plane of existance """
        pass
    
    

    def callback_client_handle(self, connection_object, data):
        # print("Server: Recieved data \""+str(data)+"\" from client \")
        # use the data to determine what connection is giving the command and if they are logged in.

        if isinstance(data, Command): # the data we recieved was a command. process it.
            if data.command == 'login':
                if data.args[0] == 'password': # TODO: put an actual password system in.
                    print('password accepted for ' + str(data.ident))
                    # from here the connection needs to create or pick a character.
                    # login accepted. Send list of the connection's characters.
                    self.callback_client_send(connection_object, 'login accepted')
                else:
                    print('password not accepted.')
                    connection_object.disconnect()

            if data.command == 'request_room':
                # sends a full update of the current room to the Connection
                # get character of connection
                self.callback_client_send(connection_object, '')

            if data.command == 'new_character':
                # player wants to make a new character.
                first = data.args[0]
                last = data.args[1]
                # after creation save it and resend them the character select screen
                # with thr new character added

            if data.command == 'request_character':
                # Connection is asking for us to load a charcter for them.
                # send it to them AND load it into active characters
                pass

            # all the commands that are actions need to be put into the command_queue then we
            #  will loop through the queue each turn and process the actions.
            if data.command == 'ping':
                self.callback_client_send(connection_object, 'pong')

            if data.command == 'move_character':
                pass

            if data.command == 'bash':
                # characters can bash certain items to break them down for crafting.
                pass

            if data.command == 'calculated_move':
                pass

            if data.command == 'move_item_to_character_storage':
                pass
        else:
            print('Connection sent invalid data.', str(data))

        return super(Server, self).callback_client_handle(connection_object, data)

    def callback_client_send(self, connection_object, data, compression=True):
        #print("Server: Sending data \""+str(data)+"\" to client \""+str(connection_object.address)
        # +"\" with compression \""+str(compression)+"\"!")
        return super(Server, self).callback_client_send(connection_object, data, compression)

    def callback_connect_client(self, connection_object):
        print("Server: Client from \""+str(connection_object.address)+"\" connected.")
        return super(Server, self).callback_connect_client(connection_object)

    def callback_disconnect_client(self, connection_object):
        print("Server: Client from \""+str(connection_object.address)+"\" disconnected.")
        return super(Server, self).callback_disconnect_client(connection_object)




if __name__ == "__main__":
    server = Server()
    server.connect('localhost', 6456)
    server.accepting_allow()

    dont_break = True
    time_offset = 1.0 # 0.5 is twice as fast, 2.0 is twice as slow
    last_turn_time = time.time()

    print('Started up Looming Darkness MUGM Server.')
    while dont_break:
        try:
            while(time.time() - last_turn_time < time_offset): # try to keep up with the time.
                time.sleep(.001)
            server.compute_turn() # where all queued creature actions get taken care of.
            last_turn_time = time.time() # based off of system clock.
        except KeyboardInterrupt:
            print('cleaning up before exiting.')
            server.accepting_disallow()
            server.disconnect_clients()
            server.disconnect()
            dont_break = False
            print('done cleaning up.')
