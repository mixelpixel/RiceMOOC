# BLACKJACK, pdk, started: 5/12/16 @ 4pm, finished @ ???
# --------------------------------------------------------------------72
import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(this, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            this.suit = suit
            this.rank = rank
        else:
            this.suit = None
            this.rank = None
            print "Invalid card: ", suit, rank

    def __str__(this):
        return this.suit + this.rank

    def get_suit(this):
        return this.suit

    def get_rank(this):
        return this.rank

    def draw(this, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(this.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(this.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        '''initializes a list of cards'''
        self.cards = []
    def __str__(self):
        '''returns the suit and rank of the list of cards in the Hand'''
        msg = ''
        if len(self.cards) == 0:
            return "You don't have any cards yet, silly!"
        else:
            for i in self.cards:
                msg += i.__str__() + ' '
            return "Hand contains: " + msg[0:-1] #chops the empty space
    def add_card(self, card):
        '''adds a Card to the Hand'''
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        pass	# compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        pass	# create a Deck object

    def shuffle(self):
        # shuffle the deck 
        pass    # use random.shuffle()

    def deal_card(self):
        pass	# deal a card object from the deck
    
    def __str__(self):
        pass	# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play

    # your code goes here
    
    in_play = True

def hit():
    pass	# replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric