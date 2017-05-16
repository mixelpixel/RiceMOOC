# MEMORY, pdk, 5/3/16 @ 10pm
# --------------------------------------------------------------------72
# -import modules
import simplegui
import random
# helper function to initialize globals
turns = 0
card1 = None
card2 = None
def new_game():
    global cards, exposed, state, turns
    cards = range(8) + range(8)
    random.shuffle(cards)
    exposed = []
    for card in range(len(cards)):
        exposed.append(False)
    state = 0
    turns = 0
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, turns, card1, card2
    for card in range(len(cards)):
        if 50 * card <= pos[0] < card * 50 + 50:
            if exposed[card] == False:
                exposed[card] = True
                if state == 0:
                    state = 1
                    card1 = cards[card]
                elif state == 1:
                    state = 2
                    card2 = cards[card]
                else:
                    state = 1
                    turns +=1
                print turns, state

                            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards
    for card in range(len(cards)):
        canvas.draw_text(str(cards[card]),
                         [card * 50 + 5, 75], 75, 'yellow')
    for card in range(len(cards)):
        if exposed[card] == False:
            canvas.draw_polygon([[50 * card, 0], [card * 50 + 50, 0],
                                 [50 * card + 50, 100], [50 * card, 100]],
                                5, 'yellow', 'green')
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric