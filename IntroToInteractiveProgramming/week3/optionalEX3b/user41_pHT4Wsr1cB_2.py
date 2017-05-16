# Reflex tester

###################################################
# Student should add code where relevant to the following.

import simplegui 

total_ticks = 0
first_click = True


# Timer handler
def tick():
    global total_ticks
    total_ticks +=1
    
# Button handler
def click():
    global first_click
    global total_ticks
    if first_click:
        timer.start()
        first_click = False
    else:
        timer.stop()
        print 'It took you ' + str(total_ticks)\
        + '/100ths of a second'
        total_ticks = 0
        first_click = True


# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()
