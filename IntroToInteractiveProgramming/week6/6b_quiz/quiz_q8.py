slow = 1000
fast = 1
year = 1

while slow > fast:
    year +=1
    slow = (slow * 2) - ((slow * 2) * .4)
    fast = (fast * 2) - (fast * 2) * .3
    print year, slow, fast
