# "PONG!"
# a simple version of the classic arcade game
# event driven and interactive
# by pk, 2016/4/21@12:30pm
# --------------------------------------------------------------------72

#-import(s)
import simplegui
import random

#-initialize global binding(s)
##- pos and vel encode vertical info for paddles
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 20
PAD_WIDTH, PAD_HEIGHT = 8, 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT, RIGHT = False, True

## initialize ball_pos and ball_vel for new bal in middle of table
## if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel ##these are vectors stored as lists

#-define helper function(s)

#-define classes
#-define event handler(s)
#up arrow and down arrow up and down key
#w and s up and down key

#-define draw handler
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel ##these are numbers
    global score1, score2 ##these are ints

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, 'green')
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, 'green')
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],
                     [WIDTH - PAD_WIDTH, HEIGHT], 1, 'green')
        
    # update ball
            
    # draw ball
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2],
                       BALL_RADIUS, 1, 'green', 'white')
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    canvas.draw_polygon([[0, (HEIGHT / 2) + HALF_PAD_HEIGHT],
                         [0, (HEIGHT / 2) - HALF_PAD_HEIGHT],
                         [PAD_WIDTH, (HEIGHT / 2) - HALF_PAD_HEIGHT],
                         [PAD_WIDTH, (HEIGHT / 2) + HALF_PAD_HEIGHT]],
                        1, 'green', 'white')
    canvas.draw_polygon([[WIDTH, (HEIGHT / 2) + HALF_PAD_HEIGHT],
                         [WIDTH, (HEIGHT / 2) - HALF_PAD_HEIGHT],
                         [WIDTH - PAD_WIDTH, (HEIGHT / 2) - HALF_PAD_HEIGHT],
                         [WIDTH - PAD_WIDTH, (HEIGHT / 2) + HALF_PAD_HEIGHT]],
                        1, 'green', 'white')
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel

def keyup(key):
    global paddle1_vel, paddle2_vel



#-create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

#-register event handler(s)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

#-start frame
new_game()
frame.start()


