# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.
import random
def powerball():
    print "Today's numbers are %d, %d, %d, %d, and %d. \
The Powerball number is %d." % (
        random.randrange(1,60),random.randrange(1,60),\
        random.randrange(1,60),random.randrange(1,60),\
        random.randrange(1,60),random.randrange(1,60))


###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()
