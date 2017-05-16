# GUI-based version of RPSLS
###################################################
# Student should add code where relevant to the following.
import simplegui
import random
# Functions that compute RPSLS
def name_to_number(name):
    '''individually converts five specific names
    exclusively to the numbers 0 through 4'''
    if name == 'rock':
        number = 0
        return number
    elif name == 'Spock':
        number = 1
        return number
    elif name == 'paper':
        number = 2
        return number
    elif name == 'lizard':
        number = 3
        return number
    elif name == 'scissors':
        number = 4
        return number
    else:
        print 'There is a problem with the names'

def number_to_name(number):
    '''converts only the numbers zero through
    four to one of five specific names'''
    if number == 0:
        name = 'rock'
        return name
    elif number == 1:
        name = 'Spock'
        return name
    elif number == 2:
        name = 'paper'
        return name
    elif number == 3:
        name = 'lizard'
        return name
    elif number == 4:
        name = 'scissors'
        return name
    else:
        print 'There is a number out of range'

def rpsls(player_choice):
    """Can you beat the computer? Enter 'rock'
    'paper' 'scissors' 'lizard' or 'Spock'"""
    print 'Player chooses %s'% player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print 'Computer chooses %s'% comp_choice
    match = (player_number - comp_number) % 5
    if match == 0:
        print "Player and computer tie!"
    elif (match == 1) or (match == 2):
        print "Player wins!"
    else:
        print "Computer wins!"
    print

# Handler for input field
def get_guess(guess):
    if guess not in ['rock', 'paper', 'scissors',
                     'lizard', 'Spock']:
        print 'Bad input "' + guess + '" to rpsls'
        print
    else:
        rpsls(guess)

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)
# Start the frame animation
frame.start()

###################################################
# Test
get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")
###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.
#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
