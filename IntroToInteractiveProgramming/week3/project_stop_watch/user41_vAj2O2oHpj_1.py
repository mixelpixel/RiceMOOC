# template for "Stopwatch: The Game"
import simplegui
# define global variables


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def timer_start():
    pass

def timer_stop():
    pass

def timer_reset():
    pass

# define event handler for timer with 0.1 sec interval


# define draw handler
def draw(canvas):
    canvas.draw_text(format, [50, 85], 20, 'green')
    
# create frame
frame = simplegui.create_frame('Stop Watch!', 150, 150)
button_start = frame.add_button('Start', timer_start, 50)
button_stop = frame.add_button('Stop', timer_stop, 50)
button_reset = frame.add_button('Reset', timer_reset, 50)

# register event handlers

# start frame
frame.start()

# Please remember to review the grading rubric
