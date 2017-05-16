# Vector addition function

###################################################
# Student should enter code below
def add_vector(v, w):
    ''' takes two 2D vectors, v and w, and returns
    their sum as a new 2D vector '''
    return [v[0] + w[0], v[1] + w[1]]



###################################################
# Test

print add_vector([4, 3], [0, 0])
print add_vector([1, 2], [3, 4])
print add_vector([2, 3], [-6, -3])



###################################################
# Output

#[4, 3]
#[4, 6]
#[-4, 0]

