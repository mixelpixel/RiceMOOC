"""
#- "Merge function for 2048 game." by pdk
#- started on 160601@0230>0430 & 1400>1600; finished on 160601@1600
#- For Coursera: Rice U. Principles of Computing pt.1
#---#----1----#----2----#----3----#----4----#----5----#----6----#----7-2--#----8----#----91234567100
Left to do, clean up the "slide_list" logic and lose fluff, submit to owl and lti test.
"""

def merge(line):
    '''
    Function that merges a single row or column in 2048.

    # models the process of merging all of the tile values
    # in a single row or column. This function takes the list line
    # as a parameter and returns a new list with the tile values
    # from line slid towards the front of the list and merged.
    # Note that you should return a new list and
    # you should not modify the input list.

    # Start with a result list that contains the same
    # number of 0's as the length of the line argument.
    '''
    result_list = [0]
    print 'Initializing and Binding a "result list" to:', result_list
    result_list *=len(line)
    print 'result_list * len(line) =', result_list
    '''
    # Iterate over the line input looking for non-zero entries.
    # For each non-zero entry, put the value into the next available
    # entry of the result list (starting at position 0).
    '''
    result_index_number = 0
    line_index = 0 # only used for print staements
    for item in line:
        print 'Merge(line)\'s index #', line_index, '- its value is', item
        line_index +=1 # only used for print statements
        if item != 0:
            print 'Placing', item, 'in result_list at INDEX', result_index_number 
            result_list[result_index_number] = item
            print 'one move at a time, result_list now:', result_list
            result_index_number +=1
            print 'increasing the result_list placement INDEX to', result_index_number
        elif item == 0:
            print 'So, we\'re skipping right along.........'
    print line
    print result_list
    print 'Done with phase #1'
    print 'should we del(resulting_index_number)?'
    print

    '''
    # Now you should think through what you should add to your function
    # in order to merge tiles. Keep in mind, however, that any tile should
    # only be merged once and that these merges should happen in order
    # from lowest index to highest index. For instance, on the input
    # [2, 0, 2, 4], the result should be [4, 4, 0, 0], not [8, 0, 0, 0].
    '''
    second_result_list = []
    slide_list = []
    print 'Initializing and Binding a 2nd_result_list to:', second_result_list
    for moved_items in result_list:
        second_result_list.append(moved_items)
    for moved_items in result_list: # FOR PRINTING _ SEE IF RESULT LIST CAN KEEP
        slide_list.append(moved_items) # SLIDE VALUES UNTIL THE END
        # OR IF I HAVE TO CHANGE RESULT LIST IN THE FOLLOWING FOR:IF LOGIC

    print 'And now 2nd_result_list matches the result_list:', second_result_list
    result_list_index = 0 # only used for print staements
    for indice in range(len(result_list[:-1])):
        print 'result_list index #', result_list_index, '- its value is', result_list[indice]
        print 'result_list index #', result_list_index + 1, '- its value is', result_list[indice + 1]
        result_list_index +=1 # only used for print staements
        if result_list[indice] == result_list[indice + 1]:
            print 'result_list INDEX', indice, '=', result_list[indice], 'and'
            print 'result_list INDEX', indice + 1, '=', result_list[indice + 1], 'so...'
            print 'result_list INDEX', indice, '== result_list INDEX', indice + 1
            second_result_list[indice] = result_list[indice] + result_list[indice + 1]
            ###IS THERE A WAY TO DO THIS WITHOUT CHANGING RESULT LIST?????
            ###OR ADDING ANOTHER LIST???
            result_list[indice] = result_list[indice] + result_list[indice + 1]
            result_list[indice + 1] = 0
            second_result_list[indice + 1] = 0
            print '2nd_result_list has merged result_list INDEXes', indice, 'and', indice + 1
            print second_result_list
        elif result_list[indice] != result_list[indice + 1]:
            print 'Moving along the indexes...'
    print line
    print result_list
    print second_result_list
    print 'Done with phase #2'
    print

    third_result_list = [0]
    print 'Initializing and Binding a 3rd_result_list to:', third_result_list
    third_result_list *=len(second_result_list)
    print '3nd_result_list * len(result_list) =', third_result_list

    '''
    # Iterate over the line input looking for non-zero entries.
    # For each non-zero entry, put the value into the next available
    # entry of the result list (starting at position 0).
    '''
    third_result_index_number = 0
    second_result_list_index = 0 # only used for print staements
    for seconds in second_result_list:
        print '2nd_result_list index #', second_result_list_index, '- its value is', seconds
        second_result_list_index +=1 # only used for print statements
        if seconds != 0:
            print 'Placing', seconds, 'in 3rd_result_list at INDEX', third_result_index_number 
            third_result_list[third_result_index_number] = seconds
            print 'one move at a time, result_list now:', third_result_list
            third_result_index_number +=1
            print 'increasing the result_list placement INDEX to', third_result_index_number
        elif seconds == 0:
            print 'So, we\'re skipping right along.........'
    print line
    print result_list
    print second_result_list
    print third_result_list
    print 'Done with phase #3'
    print
    print 'replacing result_list with third_result_list'
    print 'Start: ', line#,result_list, 'WHERE\'S THE [2, 2, 2, 0]?????????'
    print 'Slide: ', slide_list
    print 'Merge: ', third_result_list
    result_list = third_result_list
    print 'Finish:', result_list
##    del(result_index_number)
##    del(line_index)
##    del(indice)
##    del(seconds)
##    del(item)
##    del(line) #del(etc.)??????????????
    return result_list



#list_to_be_merged = [2, 0, 2, 2]
#print "list to be merged by merge(list):", list_to_be_merged
#print 'length of list to be merged', len(list_to_be_merged)
#print 'EXECUTING THE merge(line) FUNCTION:\n', merge(list_to_be_merged)
#print
#print
#print
#
#list_to_be_merged = [4, 0, 2, 0, 0, 4, 2]
#print "list_to_be_merged:", list_to_be_merged
#print 'length of list to be merged', len(list_to_be_merged)
#print 'EXECUTING THE FUNCTION:\n', merge(list_to_be_merged)
#print
#print
#print
#
#list_to_be_merged = [0, 0, 0, 2, 0, 0, 2, 0, 0, 4, 4, 2]
#print "list_to_be_merged:", list_to_be_merged
#print 'length of list to be merged', len(list_to_be_merged)
#print 'EXECUTING THE FUNCTION:\n', merge(list_to_be_merged)
#

