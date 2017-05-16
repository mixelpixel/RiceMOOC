# GUI with buttons to manipulate global variable count

###################################################
# Student should enter their code below
import simplegui

# Define event handlers for four buttons
def reset():
    '''sets global count value to zero; no return'''
    global count
    count = 0

def increment():
    '''global count plus one; no return'''
    global count
    count +=1

def decrement():
    '''global count minus one; no return'''
    global count
    count -=1

def print_count():
    '''prints variable count, no return'''
    print count
    
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame('plus or minus: 1', 200, 200)
button1 = frame.add_button('Plus 1', increment, 50)
button2 = frame.add_button('Minus 1', decrement, 50)
button3 = frame.add_button('Reset to 0', reset, 50)
button4 = frame.add_button('Print', print_count, 50)

# Start the frame animation
frame.start()

    
###################################################
# Test

# Note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Expected output from test

#1
#2
#-2
