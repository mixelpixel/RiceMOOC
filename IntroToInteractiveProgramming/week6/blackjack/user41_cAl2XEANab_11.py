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
RANKS = ('A', '2', '3', '4', '5', '6', '7',
         '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
          '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

class Card:
    def __init__(this, suit, rank):
        ''' initializes a card with suit and rank '''
        if (suit in SUITS) and (rank in RANKS):
            this.suit = suit
            this.rank = rank
        else:
            this.suit = None
            this.rank = None
            print "Invalid card: ", suit, rank
    def __str__(this):
        ''' returns the card suit and rank '''
        return this.suit + this.rank
    def get_suit(this):
        ''' returns the card suit '''
        return this.suit
    def get_rank(this):
        ''' returns the card rank '''
        return this.rank
    def draw(this, canvas, pos):
        ''' draws the card from the composite image '''
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(this.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(this.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE,
                          [pos[0] + CARD_CENTER[0],
                           pos[1] + CARD_CENTER[1]], CARD_SIZE)        

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
        ''' calculates the total score of a blackjack hand;
        the logic handles Aces being either one or eleven '''
        aces = 'A' in (i.get_rank() for i in self.hand_card)
        hand_score = sum([VALUES[i.get_rank()] for i in self.hand_card])
        if aces and hand_score + 10 <= 21:
            hand_score +=10
        return hand_score
   
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards

class Deck:
    def __init__(self):
        ''' initializes a deck of 52 cards by suit and rank order '''
        self.card_deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]
    def shuffle(self):
        ''' shuffles the deck '''
        random.shuffle(self.card_deck)
    def deal_card(self):
        ''' deals one card by popping off the last item '''
        return self.card_deck.pop()
    def __str__(self):
        ''' prints all the cards in the deck, L>R = bottom to top '''
        if len(self.card_deck) == 0:
            return 'There are no cards in the deck, silly!'
        else:
            msg = ''
            for i in self.card_deck:
#                msg += i.get_suit() + i.get_rank() + ' '
#				msg += str(i) + ' '
                msg += i.__str__() + ' '
            return 'The Deck contains ' + str(len(self.card_deck)) + ' cards: ' + msg[0:-1]

#define event handlers for buttons
def deal():
    ''' shuffles the deck and deals two cards to both
    the dealer and the player '''
    global outcome, in_play

    # your code goes here
    global blackjack_deck, player_hand, dealer_hand
    blackjack_deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    blackjack_deck.shuffle()    
    player_hand.add_card(blackjack_deck.deal_card())
    dealer_hand.add_card(blackjack_deck.deal_card())
    player_hand.add_card(blackjack_deck.deal_card())
    dealer_hand.add_card(blackjack_deck.deal_card())

    in_play = True
#    outcome = 'Player ' + player_hand.__str__() + "\nDealer " + dealer_hand.__str__()
    outcome = 'Player ' + str(player_hand) + '\nDealer ' + str(dealer_hand)
    print outcome

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