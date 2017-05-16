'''
2048merge() version2 by pdk
started on 150601@2100; finished on 150601@2230

merge a list by sliding all nonzero integers to the left,
maintaining list length by padding zeros after the slide.
If any two adjacent integers are identical, then add them together
and slide all non-zero integers to the left again while
maintaining the list length by padding zeros after the slide.
'''
# version = 2048merge.v2

def merge(line):
    '''
    This function slides nonzeros to the left, then
    adds any adjacent integers with the sum to the left
    and replacing the second integer with a zero
    and then sliding nonzeros to the left again while
    returning a list of the same length with padded
    zeros on the right (higher index)
    '''
    print line, 'merge() function argument parameter'

    '''
    slide non-zeroes
    '''
    slide_list = []
    [slide_list.append(item) for item in line if item != 0]
    print slide_list, 'slide to the left over zeros'

    '''
    merge adjacent equals
    '''
    merge_list = []
    for number in range(len(slide_list[:-1])):
        if slide_list[number] == slide_list[number + 1]:
            merge_list.append(slide_list[number] + slide_list[number + 1])
            slide_list[number + 1] = 0
        else:
            merge_list.append(slide_list[number])
    merge_list.append(slide_list[-1])
    print merge_list, 'if any adjacent duplicates, merged leaving a zero'

    '''
    slide the merged list
    '''
    result_list = []
    [result_list.append(item) for item in merge_list if item != 0]
    while len(line) > len(result_list):
        result_list.append(0)
    print result_list, 'merged list, slid over zeros with padding'

    return result_list

test1 = [2, 0, 2, 2]
print "list to be merged:", test1
print 'length of list to be merged', len(test1)
print 'EXECUTING THE FUNCTION:\n', merge(test1)
print
test2 = [4, 0, 2, 0, 0, 4, 2]
print "list to be merged:", test2
print 'length of list to be merged', len(test2)
print 'EXECUTING THE FUNCTION:\n', merge(test2)
print
test3 = [0, 0, 0, 2, 0, 0, 2, 0, 0, 4, 4, 2]
print "list to be merged:", test3
print 'length of list to be merged', len(test3)
print 'EXECUTING THE FUNCTION:\n', merge(test3)
