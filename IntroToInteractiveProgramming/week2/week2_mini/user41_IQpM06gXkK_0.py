# The objective of this program:
# Play 'guess the number' with the computer
# randomly generating from either
# [0, 100) or [0, 1000)
# Program author: Patrick Kennedy
# Start date: 2016/04/10 @ 4:30pm
# End date: 

# import statements (as needed)
import simplegui
import math
import random

# 7 steps for building an interactive program:
# 1) initialize globals
comp_num100 = random.randrange(0,100)
comp_num1000 = random.randrange(0,1000)

# 2) define helper functions

# 3) define classes (n/a)
# 4) initialize event handlers (and timers)

# 5) create a frame
frame = simplegui.frame("Guess a number", 200, 200)
#button
#enter_text

# 6) register event handlers

# 7) start frame
#start.frame()