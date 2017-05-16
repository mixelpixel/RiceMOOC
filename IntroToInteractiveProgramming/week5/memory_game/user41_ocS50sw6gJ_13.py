# MEMORY, pdk, 5/3/16 @ 10pm
# --------------------------------------------------------------------72
# -import modules
import simplegui
import random
# helper function to initialize globals
def new_game():
    global cards, exposed, state, card1, card2, turns
    cards = range(8) + range(8)
    random.shuffle(cards)
    exposed = []
    for card in range(len(cards)):
        exposed.append(False)
    state = 0
    card1 = None
    card2 = None
    turns = 0
    label.set_text("Turns = " + str(turns))
# define event handlers
def mouseclick(pos):
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
        if cards[card1] != cards[card2]:
            exposed[card1] = False
            exposed[card2] = False
        if exposed[card] == False and card != card1\ #SOMETHING IS WRONG HERE
            and card != card2:
            exposed[card] = True
            card1 = card
            card2 = None
        state = 1
        turns +=1
        label.set_text("Turns = " + str(turns))
def draw(canvas):
    global cards
    for card in range(len(cards)):
        canvas.draw_text(str(cards[card]),
                         [card * 50 + 5, 75], 75, 'yellow')
    for card in range(len(cards)):
        if exposed[card] == False:
            canvas.draw_polygon([[50 * card, 0],
                                 [card * 50 + 50, 0],
                                 [50 * card + 50, 100],
                                 [50 * card, 100]],
                                5, 'yellow', 'green')
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


# Always remember to review the grading rubric