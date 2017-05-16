# Image positioning problem
import simplegui
# global constants
WIDTH = 400
HEIGHT = 300
posw = WIDTH/2
posh = HEIGHT/2
# load test image
im = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png')
# mouseclick handler
def click(pos):
    global posw, posh
    posw = list(pos)[0]
    posh = list(pos)[1]
# draw handler
def draw(canvas):
    canvas.draw_image(im, (95/2, 93/2), (95, 93),
                      (posw, posh), (95, 93))
# create frame and register draw handler
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# start frame
frame.start()
        
                                       