# MEMORY, pdk, 5/3/16 @ 10pm
# implementation of card game - Memory
import simplegui
import random
# helper function to initialize globals
def new_game():
    global cards
    cards = range(8) + range(8)
#    random.shuffle(cards)
    print cards
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
                            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards
    for card in cards:
        canvas.draw_text(str(card), [cards.index(card) * 50 + 10, 75], 75, 'yellow')

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