# Compute whether a person is cool.

###################################################
# Is cool formula
# Student should enter function on the next lines.
def is_cool(name):
    """returns True if name is either
    "Joe", "John" or "Stephen"
    and returns False otherwise."""
#method using "or" comparison
#    if name == "Joe" or name == "John" or name == "Stephen":
#        return True
#	else:
#        return False

#method using list search
    name_list = ["Joe","John","Stephen"]
    if name in name_list:
        return True
    else:
        return False


###################################################
# Tests
# Student should not change this code.

def test(name):
    """Tests the is_even function."""
    
    if is_cool(name):
        print name, "is cool."
    else:
        print name, "is not cool."

test("Joe")
test("John")
test("Stephen")
test("Scott")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe is cool.
#John is cool.
#Stephen is cool.
#Scott is not cool.
