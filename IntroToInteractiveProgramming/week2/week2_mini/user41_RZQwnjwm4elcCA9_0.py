# The objective of this program:
# Play 'guess the number' with the computer
# randomly generating from either
# [0, 100) or [0, 1000)
# Program author: pk
# Start date: 2016/04/10 @ 4:30pm
# End date: 2016/04/12 @ 4:30pm
#-------------------------------------------
# 7 steps for building an interactive program:
# 1) import statement(s) & initialize global variable(s)
import simplegui
import math
import random

secret_number = random.randrange(0,100)
counter = 7
match = 100

# 2) define helper function(s)
def new_game():
    ''' loads variables for a new game'''
    global secret_number
    global counter
    global match
    print 'Choose a number from zero to ' + str(match)

# 3) define class(es) - (n/a)
# 4) define event handler(s) (and timer(s))
def comp100():
    ''' computer range [0, 100) '''
    global secret_number
    global counter
    global match
    secret_number = random.randrange(0,100)
    counter = 7
    match = 100
    print 'Choose a number from zero to ' + str(match)
    
def comp1000():
    ''' computer range [0, 1000) '''
    global secret_number
    global counter
    global match
    secret_number = random.randrange(0,1000)
    counter = 10
    match = 1000
    print 'Choose a number from zero to ' + str(match)
    
def counter_decrement():
    ''' counter countdown by one '''
    global counter
    counter -=1

def input_guess(guess):
    ''' main game logic '''
    counter_decrement()
    print 'Your guess was ' + guess
    guess = int(guess)
    if guess ==  secret_number:
        if (match == 100 and counter == 6) or (match == 1000 and counter == 9):
            print 'First try, NICE!'
        print 'You guessed it, ' + str(secret_number) + '!'
        print 'Play again? Just enter a number...'
        print
        if match == 1000:
            comp1000()
        else: comp100()
    elif counter == 0:
        print 'Sorry, that was your last guess'
        print 'The number was: ' + str(secret_number)
        print 'Enter a new number to play again!'
        print
        if match == 1000:
            comp1000()
        else: comp100()
    elif guess < secret_number:
        print 'Guess again: higher'
        print str(counter) + ' more guesses'
        print
    else:
        print 'Guess again: lower'
        print str(counter) + ' more guesses'
        print

# 5) create a frame (with buttons, inputs, labels, etc...)
frame = simplegui.create_frame("Guess a number", 200, 200)
guess = frame.add_input('Enter your guess', input_guess, 50)
button1 = frame.add_button('Range [0, 100)', comp100, 150)
button2 = frame.add_button('Range [0, 1000)', comp1000, 150)

# 6) register event handler(s)
# 7) start frame (and timer(s))
frame.start()

new_game()

