# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

import simplegui 

WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def timer_handler():
    global radius
    radius +=1
    
# Draw handler
def draw_handler(canvas):
    canvas.draw_circle([WIDTH // 2, HEIGHT // 2], radius, 1, 'white')

        
# Create frame and timer
frame = simplegui.create_frame('expand a circle', WIDTH, HEIGHT)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)

# Start timer
frame.start()
timer.start()