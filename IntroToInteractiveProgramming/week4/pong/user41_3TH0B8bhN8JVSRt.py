# "PONG!"
# a simple version of the classic arcade game
# event driven and interactive
# by pk, 2016/4/21@12:30pm - 11:00pm
# --------------------------------------------------------------------72
# -import modules
import simplegui
import random
# -initialize global state bindings
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 20
PAD_WIDTH, PAD_HEIGHT = 8, 80
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT, RIGHT = False, True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos, paddle2_pos = 200, 200
paddle1_vel, paddle2_vel = 0, 0
score1, score2 = 0, 0
# -define helper function(s)
def spawn_ball(direction):
    ''' sets the ball in motion '''
    global ball_pos, ball_vel # -[lists]
    if direction == RIGHT:
        ball_vel[0] =  random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 3)
    if direction == LEFT:
        ball_vel[0] = -random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 3)
# -define classes (n/a)
# -define event handlers
def new_game():
    ''' starts a new game zero to zero score
    and ball in the center of the court'''
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel # -numbers
    global score1, score2 # -integers
    global ball_pos # -[lists]
    score1 = 0
    score2 = 0
    ball_pos = [WIDTH / 2, HEIGHT / 2] # -added for restart button
    left_or_right = random.randrange(0,100) # -local variable
    if left_or_right < 50: # -fun with randomness!
        spawn_ball(LEFT)
    else:
        spawn_ball(RIGHT)
def keydown(key):
    ''' key press actions: w/s vs. up/down arrows '''
    global paddle1_vel, paddle2_vel # -numbers
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -5
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 5
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -5
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 5
def keyup(key):
    ''' key release actions '''
    global paddle1_vel, paddle2_vel # -numbers
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
def button_handler():
    ''' button to start a new game '''
    new_game()
# -define draw handler
def draw(canvas):
    ''' draws 60 times per second '''
    global score1, score2, paddle1_pos, paddle2_pos # -numbers
    global ball_pos, ball_vel # -[lists]
    # -draw court mid line and paddle gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, 'green')
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, 'green')
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],
                     [WIDTH - PAD_WIDTH, HEIGHT], 1, 'green')
    # -update ball position
    ball_pos[0] +=ball_vel[0]
    ball_pos[1] +=ball_vel[1]
    # -collide and reflect off court top and bottom
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # -collide with paddles and increase ball velocity or
    # -update score and spawn new round if no collision
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos - 40 < ball_pos[1] < paddle1_pos + 40:
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            ball_pos = [WIDTH / 2, HEIGHT / 2]
            spawn_ball(RIGHT)
            score2 +=1
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if paddle2_pos - 40 < ball_pos[1] < paddle2_pos + 40:
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            ball_pos = [WIDTH / 2, HEIGHT / 2]
            spawn_ball(LEFT)
            score1 +=1
    # -draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'green', 'white')
    # -update paddles' vertical positions, keep paddle on the screen
    if paddle1_pos + paddle1_vel <= 40:
        paddle1_pos = 40
    elif paddle1_pos + paddle1_vel >= 360:
        paddle1_pos = 360
    else:
        paddle1_pos +=paddle1_vel
    if paddle2_pos + paddle2_vel <= 40:
        paddle2_pos = 40
    elif paddle2_pos + paddle2_vel >= 360:
        paddle2_pos = 360
    else:
        paddle2_pos +=paddle2_vel
    # -draw paddles
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
    # -draw scores
    if score1 < 10:
        canvas.draw_text(str(score1), [225, 75], 100, 'green', 'monospace')
    elif score1 >9:
        canvas.draw_text(str(score1), [175, 75], 100, 'green', 'monospace')
    canvas.draw_text(str(score2), [320, 75], 100, 'green', 'monospace')
# -create frame
frame = simplegui.create_frame('PONG!', WIDTH, HEIGHT)
# -register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button = frame.add_button("Restart", button_handler)
# -start frame
new_game()
frame.start()

