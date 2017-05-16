# Define a function that returns formatted minutes and seconds

###################################################
# Circle area formula
# Student should enter function on the next lines.
def format_time(t):
    m = t // 60
    s = t % 60
    return str(m) + ' minutes and ' + str(s) + ' seconds'


###################################################
# Tests

print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)

###################################################
# Output to console
#0 minutes and 23 seconds
#20 minutes and 37 seconds
#0 minutes and 0 seconds
#31 minutes and 0 seconds
