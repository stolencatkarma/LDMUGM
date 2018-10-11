import glooey
import pyglet
import argparse
from pyglet import clock
from pyglet.window import key as KEY  # KEY.UP, KEY.B

from character import Character
from command import Command
from Mastermind._mm_client import MastermindClientTCP

pyglet.resource.path = ['gfx', 'gfx/background',
                        'gfx/scrollbox/vbar/backward', 'gfx/scrollbox/vbar/forward','gfx/scrollbox/vbar/decoration','gfx/scrollbox/vbar/grip', 
                        'gfx/scrollbox/frame/decoration'
                        ]
pyglet.resource.reindex()

class Background(glooey.Background):
    def __init__(self):
        glooey.Background.__init__(self)
        self.set_appearance(
            center=pyglet.resource.texture('center.png'),
            top=pyglet.resource.texture('top.png'),
            bottom=pyglet.resource.texture('bottom.png'),
            left=pyglet.resource.texture('left.png'),
            right=pyglet.resource.texture('right.png'),
            top_left=pyglet.resource.texture('top_left.png'),
            top_right=pyglet.resource.texture('top_right.png'),
            bottom_left=pyglet.resource.texture('bottom_left.png'),
            bottom_right=pyglet.resource.texture('bottom_right.png')
            )

class loginWindow(pyglet.window.Window):
     def __init__(self):
        pyglet.window.Window.__init__(self, 854, 480, caption='Please Login')
        self.gui = glooey.Gui(self)
        self.gui.add(Background())
        # needs label for account_name, password, server IP, server PORT
        # needs input box for each.
        # once the player logs in switch to characterSelectWindow
        
        
class CustomScrollBox(glooey.ScrollBox):
    custom_alignment = 'center'
    custom_height_hint = 200

    class Frame(glooey.Frame):
        class Decoration(glooey.Background):
            custom_center = pyglet.resource.texture('scrollbox_center.png')

        class Box(glooey.Bin):
            custom_horz_padding = 2
        
    class VBar(glooey.VScrollBar):
        class Decoration(glooey.Background):
            custom_top = pyglet.resource.image('bar_top.png')
            custom_center = pyglet.resource.texture('bar_vert.png')
            custom_bottom = pyglet.resource.image('bar_bottom.png')


        class Forward(glooey.Button):
            class Base(glooey.Image):
                custom_image = pyglet.resource.image('forward_base.png')
            class Over(glooey.Image):
                custom_image = pyglet.resource.image('forward_over.png')
            class Down(glooey.Image):
                custom_image = pyglet.resource.image('forward_down.png')

        class Backward(glooey.Button):
            class Base(glooey.Image):
                custom_image = pyglet.resource.image('backward_base.png')
            class Over(glooey.Image):
                custom_image = pyglet.resource.image('backward_over.png')
            class Down(glooey.Image):
                custom_image = pyglet.resource.image('backward_down.png')

        class Grip(glooey.ButtonScrollGrip):

            class Base(glooey.Background):
                custom_top = pyglet.resource.image('grip_top_base.png')
                custom_center = pyglet.resource.texture('grip_vert_base.png')
                custom_bottom = pyglet.resource.image('grip_bottom_base.png')

            class Over(glooey.Background):
                custom_top = pyglet.resource.image('grip_top_over.png')
                custom_center = pyglet.resource.texture('grip_vert_over.png')
                custom_bottom = pyglet.resource.image('grip_bottom_over.png')

            class Down(glooey.Background):
                custom_top = pyglet.resource.image('grip_top_down.png')
                custom_center = pyglet.resource.texture('grip_vert_down.png')
                custom_bottom = pyglet.resource.image('grip_bottom_down.png')

class characterSelectWindow(pyglet.window.Window):
    def __init__(self):
        pyglet.window.Window.__init__(self, 854, 480, caption='Select/Create a Character.')
        self.gui = glooey.Gui(self)
        self.gui.add(Background())
        # eventually show the characters load-out but for now just show a list.


class mainWindow(pyglet.window.Window):
    def __init__(self, character, room): # main window needs a room and character to display properly. 
        pyglet.window.Window.__init__(self, 854, 480, caption='Looming Darkness ' + character.full_name())
        self.gui = glooey.Gui(self)
        self.gui.add(Background())

class Client(MastermindClientTCP): # extends MastermindClientTCP
    def __init__(self, first_name, last_name):
        MastermindClientTCP.__init__(self)
       
        
        self.character = None # update this when we get a character from the server.
        self.room = None # update this from the server and use it to draw what's going on.
        
        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
        
        self.mainWindow = mainWindow()
        #characterSelectWindow = characterSelectWindow()
        #loginWindow = loginWindow()
       
        

        @self.mainWindow.event
        def on_key_press(symbol, modifiers):
            if symbol == KEY.RETURN:
                print('return')
            if symbol == KEY.W:
                command = Command(self.character.name, 'move', ['north'])
                self.send(command)
            if symbol == KEY.S:
                command = Command(self.character.name, 'move', ['south'])
                self.send(command)
            if symbol == KEY.D:
                command = Command(self.character.name, 'move', ['east'])
                self.send(command)
            if symbol == KEY.A:
                command = Command(self.character.name, 'move', ['west'])
                self.send(command)


    def open_crafting_menu(self):
        list_of_known_recipes = []
        for key, value in self.RecipeManager.RECIPE_TYPES.items(): #TODO: Don't just add them all. Pull them from creature.known_recipes
            list_of_known_recipes.append(value)


    def open_movement_menu(self, pos, tile):
        #_command = Command(client.character.name, 'calculated_move', (tile['position'].x, tile['position'].y, tile['position'].z)) # send calculated_move action to server and give it the position of the tile we clicked.
        # return _command
        pass

    def open_super_menu(self, pos, tile):
        pass

    def open_blueprint_menu(self, pos, tile):
        # blueprint_menu = Blueprint_Menu(self.screen, (0, 0, 400, 496), self.FontManager, self.TileManager)
        pass 

    def open_equipment_menu(self):
        # equipment_menu = Equipment_Menu(self.screen, (0, 0, 400, 496), self.FontManager, self.TileManager, self.player.body_parts)
        pass

    def open_items_on_ground(self, pos, tile):
        # _command = Command(self.player.name, 'move_item_to_player_storage', (tile['position'].x, tile['position'].y, tile['position'].z, item.ident)) # ask the server to pickup the item by ident. #TODO: is there a better way to pass it to the server without opening ourselves up to cheating?
        # return _command
        pass


#
#   if we start a client directly
#
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Looming Darkness MUGM Client', epilog="Please start the client with a first and last name for your character.")
    parser.add_argument('--host', metavar='Host', help='Server host', default='localhost')
    parser.add_argument('--port', metavar='Port', type=int, help='Server port', default=6456)
    parser.add_argument('first_name', help='Player\'s first name', default='John')
    parser.add_argument('last_name', help='Player\'s last name', default='Doe')

    args = parser.parse_args()
    ip = args.host
    port = args.port
    first_name = args.first_name
    last_name = args.last_name

    client = Client(first_name, last_name)
    client.connect(ip, port)
    command = Command(client.character.name, 'login', ['password'])
    client.send(command)
    command = Command(client.character.name, 'request_localmap_update')
    client.send(command)
    command = None

    # if we recieve an update from the server process it. do this first.
    
    def check_messages_from_server(dt):
        next_update = client.receive(False)
        if(next_update is not None):
            if(isinstance(next_update, Character)):
                client.character = next_update # client.player is updated
            elif(isinstance(next_update, Room)): # this is the list of chunks for the localmap compressed with zlib and pickled to binary
                client.room = next_update

    def request_localmap_update(dt):
        command = Command(client.character.name, 'request_localmap_update')
        client.send(command)       
        
    def ping(dt):
        command = Command(client.character.name, 'ping')
        client.send(command)

    clock.schedule_interval(check_messages_from_server, 0.25)
    clock.schedule_interval(ping, 30.0) # our keep-alive event. without this the server would disconnect if we don't send data within the timeout for the server.
    
    
    pyglet.app.event_loop.run() # main event loop starts here.
