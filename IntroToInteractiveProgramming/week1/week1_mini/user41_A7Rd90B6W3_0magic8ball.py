# "magic 8-ball"
import random
def number_to_fortune(number):
    '''convert 0 through 7 to a fortune text'''
    fortune_list = ['Yes, for sure!','Probably yes.',
                    'Seems like yes...','Definitely not!',
                    'Probably not.','I really doubt it...',
                    'Not sure, check back later!',"I really can't tell"]
    for i in range(8):
        if number == i:
            return fortune_list[i]
        elif i==7 and number != fortune_list[i]:
            print "Number out of range, choose 0 - 7"
        else: continue
def mystical_octosphere(question):
    print question
    print 'You shake the mystical octosphere.'    
    answer_number = random.randrange(0,7)
    answer_fortune = number_to_fortune(answer_number)
    print 'The cloudy liquid swirls, and a reply comes into view...'
    print'The mystical octosphere says...'
    print answer_fortune
    print    
    
mystical_octosphere("Will I get rich?")
mystical_octosphere("Are the Cubs going to win the World Series?")

