# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]
    if direction == RIGHT:
        ball_vel[0] =  random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 3)
    if direction == LEFT:
        ball_vel[0] = -random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 3)


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    left_or_right = random.randrange(0,100)
    if left_or_right < 50:
        spawn_ball(LEFT)
    else:
        spawn_ball(RIGHT)
    paddle1_pos = 200
    paddle2_pos = 200


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, 'green')
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, 'green')
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, 'green')
        
    # update ball
    ball_pos[0] +=ball_vel[0]
    ball_pos[1] +=ball_vel[1]
    # collide and reflect off court top and bottom
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # collide with GUTTER sides, spawn new match
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        spawn_ball(LEFT)
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        spawn_ball(RIGHT)


    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'green', 'white')
    
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos - HALF_PAD_HEIGHT],
                         [0, paddle1_pos + HALF_PAD_HEIGHT],
                         [PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT],
                         [PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT]],
                        1, 'green', 'white')
    canvas.draw_polygon([[WIDTH, paddle2_pos - HALF_PAD_HEIGHT],
                         [WIDTH, paddle2_pos + HALF_PAD_HEIGHT],
                         [WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT],
                         [WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT]],
                        1, 'green', 'white')
    
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel



def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
