# "Stopwatch: The Game"
# Create an event-driven & interactive
# stop-watch game
# script author: pk
# written 2016/04/16
# --------------------------------------------------

# - import(s)
import simplegui

# - global binding(s)
total_ticks = 0
#total_ticks = 5990 #TEST leading zeroes and rollover
first_click = True

# - define helper function(s)
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

# - define event handlers for button(s)
def timer_start():
    ''' starts the timer '''
    timer.start()

def timer_stop():
    ''' stops the timer '''
    timer.stop()

def timer_reset():
    ''' resets timer to 0:00.0 '''
    global total_ticks
    total_ticks = 0

# - define event handler for timer(s)
def timer_handler():
    ''' increments a counter every 1/10th of a second '''
    global total_ticks
    total_ticks +=1
    print total_ticks

# - define draw handler(s)
def draw_handler(canvas):
    ''' draws formatted time to canvas '''
    canvas.draw_text(format_time(), [40, 80], 30, 'green')
    
# - create frame
frame = simplegui.create_frame('Stop Watch!', 150, 150)

# - register event handler(s)
button_start = frame.add_button('Start', timer_start, 50)
button_stop = frame.add_button('Stop', timer_stop, 50)
button_reset = frame.add_button('Reset', timer_reset, 50)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)

# - start frame
frame.start()

