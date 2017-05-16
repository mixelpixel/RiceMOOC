# calculating the area of a regular polygon
# n = number of sides
# s = length ('s' for all the same, "regular" polygon)

import math

def polygon(n, s):
    return (n * s**2) / (4 * math.tan(math.pi / n))

print polygon(5,7)
print polygon(7,3)
