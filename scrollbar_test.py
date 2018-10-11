import pyglet
import glooey

for folder in ['gfx/background', 'gfx/scrollbox/vbar/backward', 'gfx/scrollbox/vbar/forward','gfx/scrollbox/vbar/decoration','gfx/scrollbox/vbar/grip',  'gfx/scrollbox/frame/decoration']:
    pyglet.resource.path.append(folder)
    print('Loaded gfx folder', folder)
pyglet.resource.reindex()

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


if __name__ == '__main__':
   

    window = pyglet.window.Window()
    gui = glooey.Gui(window)

    pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
    pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

    scroll = CustomScrollBox()
    label = glooey.Label('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam justo sem, malesuada ut ultricies ac, bibendum eu neque. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean at tellus ut velit dignissim tincidunt.  Curabitur euismod laoreet orci semper dignissim. Suspendisse potenti. Vivamus sed enim quis dui pulvinar pharetra. Duis condimentum ultricies ipsum, sed ornare leo vestibulum vitae. Sed ut justo massa, varius molestie diam. Sed lacus quam, tempor in dictum sed, posuere et diam. Maecenas tincidunt enim elementum turpis blandit tempus. Nam lectus justo, adipiscing vitae ultricies egestas, porta nec diam. Aenean ac neque tortor. Cras tempus lacus nec leo ultrices suscipit. Etiam sed aliquam tortor. Duis lacus metus, euismod ut viverra sit amet, pulvinar sed urna.\n\nAenean ut metus in arcu mattis iaculis quis eu nisl. Donec ornare, massa ut vestibulum vestibulum, metus sapien pretium ante, eu vulputate lorem augue vestibulum orci. Donec consequat aliquam sagittis. Sed in tellus pretium tortor hendrerit cursus congue sit amet turpis. Sed neque lacus, lacinia ut consectetur eget, faucibus vitae lacus. Integer eu purus ac purus tempus mollis non sed dui. Vestibulum volutpat erat magna. Etiam nisl eros, eleifend a viverra sed, interdum sollicitudin erat. Integer a orci in dolor suscipit cursus. Maecenas hendrerit neque odio. Nulla orci orci, varius id viverra in, molestie vel lacus. Donec at odio quis augue bibendum lobortis nec ac urna. Ut lacinia hendrerit tortor mattis rhoncus. Proin nunc tortor, congue ac adipiscing sit amet, aliquet in lorem. Nulla blandit tempor arcu, ut tempus quam posuere eu. In magna neque, venenatis nec tincidunt vitae, lobortis eget nulla.', line_wrap=210)
    #label = glooey.Label('yayayay', line_wrap=16)
    scroll.add(label)
    gui.add(scroll)

    pyglet.app.run()