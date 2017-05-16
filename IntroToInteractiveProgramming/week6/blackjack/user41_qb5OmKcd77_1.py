# Testing template for the get_value method for Hands


import random

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)


#####################################################
# Student should insert code for Hand class here
        
class Hand:
    def __init__(self):
        ''' initializes a list as a hand of cards '''
        self.hand_card = []
    def __str__(self):
        ''' returns the suit and rank of the list of cards in the Hand '''
        msg = ''
        if len(self.hand_card) == 0:
            return "You haven't dealt any cards yet, silly!"
        else:
            for i in self.hand_card:
                msg += i.__str__() + ' '
            return 'Hand contains: ' + msg[0:-1]
    def add_card(self, from_deck):
        ''' adds a Card to the Hand '''
        self.hand_card.append(from_deck)

    def get_value(self):
        ''' calculates the total score of each hand:
        logic handles Aces being either one or eleven'''
        score = 0
#        for i in self.hand_card:
#            for key, value in VALUES.items():
#                if i.get_rank() == key:
#                        score += value
        cards = [i.get_rank() for i in self.hand_card]
        for i in self.hand_card:
#            cards = []
#            cards.append(i.get_rank())
#            aces = 0 + cards.count('A')
            if i.get_rank() == 'A' and score + 11 > 21:
                score += VALUES[i.get_rank()]
            elif i.get_rank() == 'A':
                score += VALUES[i.get_rank()] + 10
            else:
                score += VALUES[i.get_rank()]
        return score, cards

    
###################################################
# Test code

c1 = Card("S", "A")
c2 = Card("C", "2")
c3 = Card("D", "T")
c4 = Card("S", "K")
c5 = Card("C", "7")
c6 = Card("D", "A")

test_hand = Hand()
print test_hand
print test_hand.get_value()

test_hand.add_card(c2)
print test_hand
print test_hand.get_value()

test_hand.add_card(c5)
print test_hand
print test_hand.get_value()

test_hand.add_card(c3)
print test_hand
print test_hand.get_value()

test_hand.add_card(c4)
print test_hand
print test_hand.get_value()



test_hand = Hand()
print test_hand
print test_hand.get_value()

test_hand.add_card(c1)
print test_hand
print test_hand.get_value()

test_hand.add_card(c6)
print test_hand
print test_hand.get_value()

test_hand.add_card(c4)
print test_hand
print test_hand.get_value()

test_hand.add_card(c5)
print test_hand
print test_hand.get_value()

test_hand.add_card(c3)
print test_hand
print test_hand.get_value()



###################################################
# Output to console
# note that the string representation of a hand may vary
# based on your implementation of the __str__ method

#Hand contains 
#0
#Hand contains C2 
#2
#Hand contains C2 C7 
#9
#Hand contains C2 C7 DT 
#19
#Hand contains C2 C7 DT SK 
#29
#Hand contains 
#0
#Hand contains SA 
#11
#Hand contains SA DA 
#12
#Hand contains SA DA SK 
#12
#Hand contains SA DA SK C7 
#19
#Hand contains SA DA SK C7 DT 
#29