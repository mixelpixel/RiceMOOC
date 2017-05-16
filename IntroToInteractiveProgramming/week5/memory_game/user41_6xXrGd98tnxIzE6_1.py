# MEMORY, pdk, started: 5/3/16 @ 10pm, finished 5/5/16 @ 4pm
# --------------------------------------------------------------------72
import simplegui
import random

def new_game():
    ''' initialize globals, set-up game deck '''
    global cards, exposed, state, card1, card2, turns
    cards = range(8) + range(8)
    random.shuffle(cards)
    exposed = [False for card in range(len(cards))] #list comprehension
    state = 0
    card1 = None
    card2 = None
    turns = 0
    label.set_text("Turns = " + str(turns))

def mouseclick(pos):
    ''' game logic based on list value and index '''
    global state, card1, card2, turns
    card = pos[0]//50
    if state == 0:
        if exposed[card] == False:
            exposed[card] = True
            card1 = card
            state = 1
    elif state == 1:
        if exposed[card] == True:
            pass
        elif exposed[card] == False:
            exposed[card] = True
            card2 = card
            state = 2
    else:
        if exposed[card] == True:
            pass
        elif cards[card1] != cards[card2]:
            exposed[card1] = False
            exposed[card2] = False
        if exposed[card] == False:
            exposed[card] = True
            card1 = card
            card2 = None
            state = 1
            turns +=1
            label.set_text("Turns = " + str(turns))

def draw(canvas):
    ''' positions numbers and card covers '''
    global cards
    # list comprehension mapping
    [canvas.draw_text(str(cards[card]), [card * 50 + 5, 75], 75,
    'yellow') for card in range(len(cards))]
    #list comprehension filtering
    [canvas.draw_polygon([[50 * card, 0], [card * 50 + 50, 0],
    [50 * card + 50, 100],[50 * card, 100]], 5, 'yellow', 'green')\
    for card in range(len(cards)) if exposed[card] == False]

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

