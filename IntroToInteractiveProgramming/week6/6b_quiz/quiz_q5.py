##def list_extend_many(lists):
##    """Returns a list that is the concatenation of all the lists in the given list-of-lists."""
##    result = []
##    for l in lists:
##        result.extend(l)
##    print result

##def list_extend_many(lists):
##    result = []
##    i = 0
##    while i < len(lists):
##        result.extend(lists[i])
##        i += 1
##    print result

##def list_extend_many(lists):
##    result = []
##    i = 0
##    while i < len(lists):
##        result += lists[i]
##        i += 1
##    print result


##def list_extend_many(lists):
##    result = []
##    i = 0
##    while i < len(lists):
##        i += 1
##        result.extend(lists[i])
##    print result

def list_extend_many(lists):
    result = []
    i = 0
    while i <= len(lists):
        result.extend(lists[i])
        i += 1
    print result

list_extend_many([[1,2], [3], [4, 5, 6], [7]])
