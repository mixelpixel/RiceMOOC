def quiz(p, q):
    if p == False:
        return False
    elif q == False:
        return False
    else:
        return True

print quiz(True, True)
print quiz(True, False)
print quiz(False, True)
print quiz(False, False)
print '------------'

p, q = True, True
print p and q
p, q = True, False
print p and q
p, q = False, True
print p and q
p, q = False, False
print p and q
print

p, q = True, True
print p or q
p, q = True, False
print p or q
p, q = False, True
print p or q
p, q = False, False
print p or q
print

p, q = True, True
print p and (not q)
p, q = True, False
print p and (not q)
p, q = False, True
print p and (not q)
p, q = False, False
print p and (not q)
print

p, q = True, True
print (not p) and (not q)
p, q = True, False
print (not p) and (not q)
p, q = False, True
print (not p) and (not q)
p, q = False, False
print (not p) and (not q)




