# Rock-paper-scissors-lizard-Spock template
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random

def name_to_number(name):
    """individually converts five specific names
    exclusively to the numbers 0 through 4"""
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
    elif name == 'spock':
        print '"%s"%s? Even fictional characterS deServe'%(name[0],name[1:])
        print 'to have their proper nounS capitalized ;)'
    else:
        print '"%s" is not a valid name. Please enter one'%name
        print 'of the following into the rspls() function:'
        print "'rock',"
        print "'Spock',"
        print "'paper',"
        print "'lizard', or "
        print "'scissors'"

def number_to_name(number):
    """converts only the numbers zero through
    four to one of five specific names"""
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

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




