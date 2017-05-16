def appendsums(lst):
    for num in range(25):
        print num
        lst.append(sum(list(lst[-3:])))
        print lst
##            lst.append(sum(lst[-3]))
##    return lst
sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[10]
print sum_three[20]
