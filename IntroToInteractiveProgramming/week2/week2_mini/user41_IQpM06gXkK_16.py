# The objective of this program:
# Play 'guess the number' with the computer
# randomly generating from either
# [0, 100) or [0, 1000)
# Program author:
# Start date: 2016/04/10 @ 4:30pm
# End date: 
#-------------------------------------------
# import statements (as needed)
import simplegui
import math
import random

# 7 steps for building an interactive program:
# 1) initialize global variable(s)
secret_number = random.randrange(0,100)
comp100 = random.randrange(0,100)
comp1000 = random.randrange(0,1000)
counter = 7

# 2) define helper function(s)
def new_game():
    global secret_number
#    counter_advance()
    counter_decrement()

# 3) define class(es) - (n/a)
# 4) define event handler(s) (and timer(s))
def comp100():
    ''' computer range [0, 100) '''
    global secret_number
    secret_number = random.randrange(0,100)

def comp1000():
    ''' computer range [0, 1000) '''
    global secret_number
    global counter
    secret_number = random.randrange(0,1000)
    counter = 10

def counter_advance():
    global counter
    counter +=1

def counter_decrement():
    global counter
    counter -=1

def input_guess(guess):
    ''' main game logic '''
    global secret_number
    global counter
#    counter_advance()
    counter_decrement()
    print 'Your guess was ' + guess
    guess = int(guess)
    if int(guess) ==  secret_number:
        print 'You guessed it, ' + str(secret_number) + '!'
        print
    elif guess < secret_number:
        global counter
        print 'Guess again: higher'
        print secret_number
        print counter
    else:
        print 'Guess again: lower'
        print secret_number
        print counter

# 5) create a frame (with buttons, inputs, labels, etc...)
frame = simplegui.create_frame("Guess a number", 200, 200)
guess = frame.add_input('Enter your guess', input_guess, 50)
button1 = frame.add_button('Range [0, 100)', comp100, 150)
button2 = frame.add_button('Range [0, 1000)', comp1000, 150)

# 6) register event handler(s)
# 7) start frame (and timer(s))
frame.start()