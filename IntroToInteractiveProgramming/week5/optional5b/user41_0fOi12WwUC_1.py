# Image positioning problem
import simplegui
# global constants
WIDTH = 400
HEIGHT = 300
click_position = (WIDTH/2, HEIGHT/2)
# load test image
asteroid = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png')
asteroid_size = (asteroid.get_width(), asteroid.get_height())
asteroid_center = (asteroid_size[0] / 2, asteroid_size[1] / 2)
# mouseclick handler
def click(pos):
    global click_position
    click_position = pos
# draw handler
def draw(canvas):
    canvas.draw_image(asteroid, asteroid_center, asteroid_size,
                      click_position, asteroid_size)
# create frame and register draw handler
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# start frame
frame.start()