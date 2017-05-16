#Challenge: Given numbers a, b, and c,
#the quadratic equation ax2+bx+c=0 can have
#zero, one or two real solutions
#(i.e; values for x that satisfy the equation).
#The quadratic formula
#x=-b +/- sqrt(b2&#8722;4ac)2a
#can be used to compute these solutions.
#The expression b2 - 4ac is the discriminant
#associated with the equation. If the discriminant
#is positive, the equation has two solutions.
#If the discriminant is zero, the equation has
#one solution. Finally, if the discriminant is negative,
#the equation has no solutions.
#Write a Python function smaller_root that
#takes an input the numbers a, b and c and returns
#the smaller solution to this equation if one exists.
#If the equation has no real solution, print the
#message "Error: No real solutions" and simply return.
#Note that, in this case, the function will actually
#return the special Python value None.



# Compute the smaller root of a quadratic equation.

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.
def smaller_root(a,b,c):
    """returns the smaller solution if one exists"""
    discriminant = b**2 - (4*a*c)
    if discriminant < 0:
        print "Error: No real solutions"
    else:
        quad_form_pos = (-b + (b**2 - 4*a*c)**.5) / (2*a)
        quad_form_neg = (-b - (b**2 - 4*a*c)**.5) / (2*a)
        if quad_form_pos > quad_form_neg:
            return quad_form_neg
        else:
            return quad_form_pos
#ALSO
#    """
#    Returns the smaller root of a quadratic equation with the
#    given coefficients.
#    """
#    
#    discriminant = b ** 2 - 4 * a * c
#    if discriminant < 0 or a == 0:
#        print "Error: No real solutions"
#    else:
#        discriminant_sqrt = discriminant ** 0.5
#        # Choose the positive or negative square root that leads to a smaller root.
#        if a > 0:
#            smaller = - discriminant_sqrt
#        else:
#            smaller = discriminant_sqrt
#        return (-b + smaller) / (2 * a)


###################################################
# Tests
# Student should not change this code.

def test(a, b, c):
    """Tests the smaller_root function."""
    
    print "The smaller root of " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " is:" 
    print str(smaller_root(a, b, c))
        

test(1, 2, 3)
test(2, 0, -10)
test(6, -3, 5)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The smaller root of 1x^2 + 2x + 3 is:
#Error: No real solutions
#None
#The smaller root of 2x^2 + 0x + -10 is:
#-2.2360679775
#The smaller root of 6x^2 + -3x + 5 is:
#Error: No real solutions
#None
