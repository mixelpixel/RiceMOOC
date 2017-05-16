# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1
    
# Event handlers for buttons    
def start():
    timer.start()

def stop():
    timer.stop()

def reset():
    global counter
    counter = 0

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(1000, tick)
button_start = frame.add_button('start', start)
button_stop = frame.add_button('stop', stop)
button_reset = frame.add_button('reset', reset)

# Start timer
#timer.start()
frame.start()