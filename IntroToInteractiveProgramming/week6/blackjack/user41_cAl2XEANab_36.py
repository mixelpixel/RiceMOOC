#- BLACKJACK, pdk, started: 5/12/16 @ 4pm, finished @ ???
#---------------------------------------------------------------------72
#- import modules
import simplegui
import random

#- declare globals
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image\
("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image\
("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    
in_play = False
outcome = ''
score = 0
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
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
        ''' initializes an empty list as a hand of cards '''
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
        for c in self.hand_card:
            c.draw(canvas, [pos[0] + self.hand_card.index(c) * (CARD_SIZE[0] - 20), pos[1]])

class Deck:
    def __init__(self):
        ''' initializes a deck of 52 cards
        by suit and rank order '''
        self.card_deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]
    def shuffle(self):
        ''' shuffles the deck '''
        random.shuffle(self.card_deck)
    def deal_card(self):
        ''' deals one card by popping off the last item
        as if it were the "top" of the deck '''
        return self.card_deck.pop()
    def __str__(self):
        ''' counts and prints all the cards in the deck
        L>R = bottom to top '''
        if len(self.card_deck) == 0:
            return 'There are no cards in the deck, silly!'
        else:
            msg = ''
            for i in self.card_deck:
                msg += str(i) + ' '
            return 'The Deck contains ' + str(len(self.card_deck)) + ' cards: ' + msg[0:-1]

#- event handlers for buttons
def deal():
    ''' shuffles the deck and deals two cards to both
    the dealer and the player '''
    global outcome, in_play, score
    if in_play:
        score -=1
        label.set_text("score = " + str(score))
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
    outcome = 'Hit or Stand?'

def hit():
    ''' if the hand is in play, hit the player
    if busted, assign a message to outcome,
    update in_play and score '''
    global in_play, outcome, score
    if in_play:
        player_hand.add_card(blackjack_deck.deal_card())
        outcome = 'Player hand = ' + str(player_hand.get_value())
        if player_hand.get_value() > 21:
            in_play = False
            score -=1
            label.set_text("score = " + str(score))
            outcome = 'BUST!!!'
    elif not in_play:
        outcome = 'Deal again?'

def stand():
    ''' if hand is in play, repeatedly hit dealer until
    dealer hand has value 17 or more; assign a message
    to outcome, update in_play and score '''
    global in_play, outcome, score
    if not in_play and outcome == 'BUST!!!':
        outcome = "Sorry, you're BUSTED!!!"
    elif in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(blackjack_deck.deal_card())
        in_play = False
        if dealer_hand.get_value() > 21:
            in_play = False
            score +=1
            label.set_text("score = " + str(score))
            outcome = 'DEALER BUSTED YOU WIN!'
        elif dealer_hand.get_value() >= player_hand.get_value():
            in_play = False
            score -=1
            label.set_text("score = " + str(score))
            outcome = 'DEALER WINS'
        else:
            in_play = False
            score +=1
            label.set_text("score = " + str(score))
            outcome = 'YOU WON!'

#- draw handler    
def draw(canvas):
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [136,98], CARD_SIZE)
        dealer_hand.draw(canvas, [100, 50])
    else:
        dealer_hand.draw(canvas, [100, 50])

    player_hand.draw(canvas, [100, 250])
    canvas.draw_text('BlackJack!', (375, 40), 50, 'black')
    canvas.draw_text('Dealer hand:', (50, 40), 25, 'black', 'sans-serif')
    canvas.draw_text('Player hand: ', (50, 240), 25, 'black', 'sans-serif')
    canvas.draw_text(outcome, (50, 375), 20, 'yellow')

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 400)
frame.set_canvas_background("Green")
label = frame.add_label('Score = ' + str(score))

# buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

#- and go!
deal()
frame.start()


''' review the grading rubric '''