# Create an event-driven and interactive stop-watch

# template for "Stopwatch: The Game"
import simplegui

# define global variables
total_ticks = 0
first_click = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format_time():
    ''' formats tenths of seconds into
    minutes:seconds.tenths, e.g.
    15 minutes, two seconds and 3-tenths of a second
    will display as 15:02.3 '''
    time_in_seconds = total_ticks / 10
    minutes = time_in_seconds // 60
    seconds = time_in_seconds % 60
    tens_seconds = seconds // 10
    ones_seconds = seconds % 10
    tenths_seconds = str(total_ticks)[-1]
    return str(minutes) + ':' + str(tens_seconds) + \
    str(ones_seconds) + '.' + tenths_seconds    

# define event handlers for buttons; "Start", "Stop", "Reset"
def timer_start():
    timer.start()

def timer_stop():
    timer.stop()

def timer_reset():
    global total_ticks
    total_ticks = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global total_ticks
    total_ticks +=1
    print total_ticks

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format_time(), [40, 80], 30, 'green')
    
# create frame
frame = simplegui.create_frame('Stop Watch!', 150, 150)
button_start = frame.add_button('Start', timer_start, 50)
button_stop = frame.add_button('Stop', timer_stop, 50)
button_reset = frame.add_button('Reset', timer_reset, 50)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# Please remember to review the grading rubric

