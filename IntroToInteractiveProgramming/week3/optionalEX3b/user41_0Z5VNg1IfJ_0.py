# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 

color = 'red'


# Timer handler
def tick():
    global color
    if color == 'red':
        color = 'blue'
    else:
        color = 'red'
    frame.set_canvas_background(color)
        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(3000, tick)
frame.set_canvas_background('red')

# Start timer
frame.start()
timer.start()
