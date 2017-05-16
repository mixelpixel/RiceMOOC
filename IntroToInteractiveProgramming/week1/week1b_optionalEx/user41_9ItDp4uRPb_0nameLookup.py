# Compute instructor's last name, given the first name.

###################################################
# Name lookup formula
# Student should enter function on the next lines.
def name_lookup(first_name):
    first_name_list = ["Joe", "Scott", "John", "Stephen"]
    last_name_list = ["Warren", "Rixner", "Greiner", "Wong"]
    if first_name in first_name_list:
        return last_name_list[first_name_list.index(first_name)]
    else:
        return "Error: Not an instructor"


#	if first_name == "Joe":
#		return "Warren"
#	elif first_name == "Scott":
#		return "Rixner"
#	elif first_name == "John":
#		return "Greiner"
#	elif first_name == "Stephen":
#		return "Wong"
#	else:
#		return "Error: Not an instructor"


###################################################
# Tests
# Student should not change this code.

def test(first_name):
    """Tests the name_lookup function."""
    
    print name_lookup(first_name)
    
test("Joe")
test("Scott")
test("John")
test("Stephen")
test("Mary")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Warren
#Rixner
#Greiner
#Wong
#Error: Not an instructor
