# Functions to manipulate global variable count

###################################################
# Student should enter function on the next lines.
# Reset global count to zero.
# Increment global count.
# Decrement global count.
# Print global count.
def reset():
    '''establish a global variable'''
    global count
    count = 0
    
def increment():
    '''modify global variable'''
    global count
    count +=1
    
def decrement():
    '''modify global variable'''
    global count
    count -=1

def print_count():
    '''print global variable'''
    global count
    print count

    
###################################################
# Test

# note that the GLOBAL count is defined inside a function
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
# Output
#1
#2
#-2