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
ball_pos = [WIDTH / 2, HEIGHT / 2]
#ball_vel = [1, -1]
#ball_vel = [1, 1]
#ball_vel = [-1, 1]
ball_vel = [-1, -1]

paddle1_pos = [[0, HEIGHT / 2 + HALF_PAD_HEIGHT],
               [0, HEIGHT / 2 - HALF_PAD_HEIGHT],
               [PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT],
               [PAD_WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT]]
paddle2_pos = [[WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT],
               [WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT],
               [WIDTH - PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT],
               [WIDTH - PAD_WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT]]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]

## if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel ##these are vectors stored as lists
    

#-define helper function(s)

#-define classes
#-define event handler(s)

#-define draw handler
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel ##these are numbers
    global score1, score2 ##these are ints
#    spawn_ball(direction)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, 'green')
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, 'green')
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],
                     [WIDTH - PAD_WIDTH, HEIGHT], 1, 'green')
        
    # update ball
    ball_pos[0] +=ball_vel[0]
    ball_pos[1] +=ball_vel[1]
    
    # collide and reflect off court top and bottom
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
#    # collide and reflect off court sides
#    if ball_pos[0] <= BALL_RADIUS:
#        ball_vel[0] = - ball_vel[0]
#    if ball_pos[0] >= WIDTH - BALL_RADIUS:
#        ball_vel[0] = - ball_vel[0]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'green', 'white')
    
    # update paddle's vertical position, #####keep paddle on the screen
    if paddle1_pos[1][1] <= 0:
        paddle1_pos[1][1] == 0
    if paddle1_pos[0][1] >=400:
        paddle1_pos[0][1] == 400
    paddle1_pos[0][1] +=paddle1_vel[1]
    paddle1_pos[1][1] +=paddle1_vel[1]
    paddle1_pos[2][1] +=paddle1_vel[1]
    paddle1_pos[3][1] +=paddle1_vel[1]

    paddle2_pos[0][1] +=paddle2_vel[1]
    paddle2_pos[1][1] +=paddle2_vel[1]
    paddle2_pos[2][1] +=paddle2_vel[1]
    paddle2_pos[3][1] +=paddle2_vel[1]

    # draw paddles
    #paddle1
    canvas.draw_polygon(paddle1_pos, 1, 'green', 'white')
    #paddle2
    canvas.draw_polygon(paddle2_pos, 1, 'green', 'white')

    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = [0, -5]
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = [0, 5]
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = [0, -5]
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = [0, 5]

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = [0, 0]
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = [0, 0]
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = [0, 0]
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = [0, 0]

#-create frame
frame = simplegui.create_frame('PONG!', WIDTH, HEIGHT)

#-register event handler(s)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

#-start frame
new_game()
frame.start()


