#- "ROCK STAR" by pdk
#- 160524@2000start; yymmdd@????finished
#- For Coursera: Rice U. Intro to Interactive Programming
#- Based on the classic arcade game, "Asteroids"
#---#----1----#----2----#----3----#----4----#----5----#----6----#----7-2--#----8----#----91234567890

import simplegui, math, random
#I'll need to remove all the instances of math. and ramdom.
#but I'd like to try this way:
#from math import sin, cos, sqrt, pi
#from random import random, choice, randrange

# globals bindings - CAPITALIZE ALL OF THEM?
WIDTH, HEIGHT = 800, 600
SCREEN_SIZE = (WIDTH, HEIGHT)
NUM_LIVES = 3 #Starting number
SAFETY = 50 #For distance calculation when spawning asteroids - decrease as game continues?
time = 0
score = 0
lives = NUM_LIVES #I'm still confused about variable bindings, except for id()...
started = False

ship_radius = 35 #I MIGHT WANT TO CHANGE THE SIZE OF THE SHIP too...
rockets_volume = 0.3

rock_group = set() #asteroid group = ({}) ?
num_of_asteroids = 8 #Increase with score? maybe timer?
asteroid_radius = 40 #decrease as game progresses?

missile_group = set() #is there a difference with x = ([]) ?
num_of_missiles = 5 # more with higher score? fire from all 5 guns?
missile_lifespan = 90
msl_thrust = 10 # faster with higher score?
missile_radius = 3
missile_volume = 0.2

explosion_group = set()

soundtrack_volume = 0.05


class ImageInfo:
    '''A Classy way of handling imagery information
    methods are just 'getters' here.'''

    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        '''initializes digital image attributes
        for the ImageInfo class'''
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        '''returns the images center (width, height)
        from the referenced grfx'''
        return self.center

    def get_size(self):
        '''returns the images size dimensions (width, height)
        from the referenced grfx'''
        return self.size

    def get_radius(self):
        '''returns the effective radius of the image
        for calculating Sprite collisions'''
        return self.radius

    def get_lifespan(self):
        '''returns the images lifespan'''
        return self.lifespan

    def get_animated(self):
        '''returns the animation status of an image sheet'''
        return self.animated

def image_and_sound_declarations():
    '''I zipped all these up into a function because they are a mess
    to look at and now I can collapse them as I work :D'''
    global splash_image, splash_info
    global debris_info, debris_image
    global nebula_info, nebula_image
    global ship_info, ship_image
    global missile_info, missile_image
    global asteroid_info, asteroid_image
    global soundtrack, missile_sound, ship_thrust_sound, explosion_sound

#THESE ARE MY IMAGES AND SOUNDS - PLEASE COMMENT OUT IF THEY DON'T LOAD - THANK YOU!!!!
    splash_info = ImageInfo([200, 150], [400, 300])
    splash_image = simplegui.load_image("https://dl.dropbox.com/s/yaazzsgnraxz5jm/my_splash.png")
    debris_info = ImageInfo([320, 240], [640, 480])
    debris_image = simplegui.load_image("https://dl.dropbox.com/s/uelrcnu4aexo2he/debris.png")
    nebula_info = ImageInfo([400, 300], [800, 600])
    nebula_image = simplegui.load_image("https://dl.dropbox.com/s/h5awm7onocm9v10/space.png")
    ship_info = ImageInfo([45, 45], [90, 90], ship_radius)
    ship_image = simplegui.load_image("https://dl.dropbox.com/s/ezp7v5d7ti7dhpg/spaceship.png")
    missile_info = ImageInfo([5,5], [10, 10], missile_radius, missile_lifespan)
    missile_image = simplegui.load_image("https://dl.dropbox.com/s/jyly627nc8v1zku/missile.png")
    asteroid_info = ImageInfo([45, 45], [90, 90], asteroid_radius)
    asteroid_image = simplegui.load_image("https://dl.dropbox.com/s/gvja7maw8ppthe9/asteroid.png")

    ###SOUND asset from http://www-pw.physics.uiowa.edu/space-audio/cassini/SKR1/
    soundtrack = simplegui.load_sound("https://dl.dropbox.com/s/41w472w2b3b4ij2/space.mp3")
    ###Original recordings by me:
    missile_sound = simplegui.load_sound("https://dl.dropbox.com/s/jciomfzbvklfzyk/pow.mp3")
    ship_thrust_sound = simplegui.load_sound("https://dl.dropbox.com/s/2298a7diby28hth/thrust.mp3")
    explosion_sound = simplegui.load_sound("https://dl.dropbox.com/s/za2gl2sk9jzqz6q/explosion.mp3")

#BELOW ARE THE COURSERA IMAGES - PLEASE UNCOMMENT IF MINE (ABOVE) DON'T WORK, THANK YOU!
#    # art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
#    # debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#    #                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
#    debris_info = ImageInfo([320, 240], [640, 480])
#    debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")
#
#    # nebula images - nebula_brown.png, nebula_blue.png
#    nebula_info = ImageInfo([400, 300], [800, 600])
#    nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")
#
#    # splash image
#    splash_info = ImageInfo([200, 150], [400, 300])
#    splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")
#
#    # ship image
#    ship_info = ImageInfo([45, 45], [90, 90], 35)
#    ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
#
#    # missile image - shot1.png, shot2.png, shot3.png
#    missile_info = ImageInfo([5,5], [10, 10], 3, 50)
#    missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
#
#    # asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
#    asteroid_info = ImageInfo([45, 45], [90, 90], 40)
#    asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
#
#    # animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
    explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
    explosion_image = simplegui.load_image(\
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

    # SOUNDS
    # sound assets purchased from sounddogs.com, please do not redistribute
    # alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
    # please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
    # sound assets purchased from sounddogs.com, please do not redistribute
    # .ogg versions of sounds are also available, just replace .mp3 by .ogg
#    soundtrack = simplegui.load_sound(\
#    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
#    missile_sound = simplegui.load_sound(\
#    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
#    ship_thrust_sound = simplegui.load_sound(\
#    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
#    explosion_sound = simplegui.load_sound(\
#    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
    pass
image_and_sound_declarations()


# helper functions
def angle_to_vector(ang):
    '''FORWARD: for acceleration in direction of the forward vector
    converts the radian angle to a vector: REVIEW TRIGONOMETRY.
    Returns a vector consisting in 2 real numbers between -1 and 1'''
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    '''returns the distance between two points in Cartesian
    coordinate space where (w, h) = (width, height)'''
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

def pos_or_neg(num):
    '''returns a POSitive OR NEGative numeric value'''
    #can also be re-written with random.uniform(-1, 1)
    #but the way I've implemented it with the rock_spawner
    #it nicely avoids zero values
    sign = random.choice([False, True]) #sign = random.choice([0,1]) also
    if sign: return num                 #works for 'false or true'
    else: return -num

def wrap(position, vector):
    """Moves the position by the given vector in
    2-Dimensional(d) toroidal space."""
    for d in range(2):
#########REPLACES THIS:
#        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
#        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        position[d] = (position[d] + vector[d]) % SCREEN_SIZE[d]

def initial_ship_orientation():
    return random.choice([0, (math.pi * .5), (math.pi), (math.pi * 1.5)])

def process_sprite_group(sprite_group, canvas):
    '''handles drawing and updates for any group of Sprites'''
    global missile_group
    if started:
        timer.start()
        for sprite in sprite_group:
            sprite.draw(canvas)
            sprite.update()
    ### NOT SURE ABOUT HANDLING THE MISSILE AGE HERE...
    ### BUT THE TIMING IS ~60 fps * missile_lifespan
    ### AND HANDLING IT IN SPRITE CLASS OR DRAW()
    ### MAKES THE LIFESPAN LONGER. NOT SURE WHY.
        for missile in list(missile_group):
            missile.age +=1
            if missile.age > missile.lifespan:
                missile_group.remove(missile)

def group_collide(group, other_object):
    '''removes a single member of a set when colliding
    with another object'''
#    for sprite in list(group):
#        if sprite.collision(other_object):
#            group.remove(sprite)
    if [group.remove(sprite) for sprite in list(group) if sprite.collision(other_object)]:
        return True

def group_group_collide(member_group, all_group):
    '''removes a member from the first set when there is
    a collision between any members of two sets'''
#    for m in list(member_group):
#        if group_collide(all_group, m):
#            member_group.remove(m)

    if [member_group.remove(m) for m in list(member_group) if group_collide(all_group, m)]:
        return True


class Ship:
    '''it spins, it thrusts, it shoots, it's AMAZING!!!'''

    def __init__(self, pos, vel, angle, image, info):
        '''initializes attributes for the Ship class instances'''
        self.pos = [pos[0],pos[1]] #Ship position
        self.vel = [vel[0],vel[1]] #Ship velocity
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0 #Radians, not degrees
        self.angle_spin = .08 #change in angular velocity
        self.image = image
        self.image_center = list(info.get_center()) #list() keeps the lives draw handler able to ref info
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.sound = ship_thrust_sound

    def torq(self, spin):
        '''method to change the angular velocity in radians
        'cw' for CLOCKWISE, 'ccw' for COUNTER-CLOCKWISE'''

        if spin == 'cw':
            self.angle_vel += self.angle_spin
        elif spin == 'ccw':
            self.angle_vel -= self.angle_spin

    def rockets(self, firing):
        '''method to handle rocket imagery and sounds'''

        self.thrust = firing
        if firing:
            self.image_center[0] += self.image_size[0]
            if started:
                self.sound.set_volume(rockets_volume)
                self.sound.rewind()
                self.sound.play()
        else: #when firing stops, return to:
            self.image_center[0] -= self.image_size[0]
            self.sound.pause()

    def shoot(self):
        '''method to spawn missiles and handle missile attributes
        for position, velocity and forward acceleration.
        "msl" = "missile"'''

        global missile_group, msl_thrust
        fwd = angle_to_vector(self.angle)
        msl_pos = [self.pos[0] + self.radius * fwd[0],
                   self.pos[1] + self.radius * fwd[1]]
        msl_vel = [self.vel[0] + msl_thrust * fwd[0],
                   self.vel[1] + msl_thrust * fwd[1]]
        if len(missile_group) < num_of_missiles:
            missile_group.add(Sprite(msl_pos, msl_vel, 0, .1,
                                     missile_image, missile_info, missile_sound))

    def draw(self,canvas):
        '''method to draw the Ship image'''
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)

    def update(self):
        '''method to handle Ship attribute updates'''

        #ANGLE - updates Ship orientation by the
        #        angular velocity (the speed at which Ship spins)
        self.angle += self.angle_vel

        #POSITION FOR TOROIDAL SPACE
        wrap(self.pos, self.vel)

        #CONSTANT FRICTION
        fric_c = .01 #BETTER WAY TO HANDLE THIS FRICASSEE FACTOR?????
        self.vel[0] *= (1 - fric_c) #I don't think friction needs to be global cuz
        self.vel[1] *= (1 - fric_c) #it only pertains to Ship(s), but it'd be easier to find & adjust

        #THRUST - ACCELERATION IN DIRECTION OF FWD VECTOR
        #based on ship orientation
        fwd_dir = angle_to_vector(self.angle)
        accel_const = 10
        if self.thrust:
            self.vel[0] += fwd_dir[0] / accel_const
            self.vel[1] += fwd_dir[1] / accel_const

class Sprite:
    '''A spritely class'''

    def __init__(self, pos, vel, ang, ang_vel,
                 image, info, sound = None):
        '''initializes attributes for the Sprite instances'''
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel #Radians, ~(2*pi = 360deg)
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound: #ONLY MISSILES HAVE SOUND, BUT WHAT ABOUT EXPLOSIONS?
            sound.rewind()
            sound.play()
            sound.set_volume(missile_volume)

    def __str__(self):
        if self.image == asteroid_image:
            return 'An asteroid'
        elif self.image == missile_image:
            return 'A missile'
        else:
            return 'A sprite'

    def draw(self, canvas):
        '''method to draw the Sprite instances'''
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)

    def update(self):
        '''method to update attributes of Sprite class instances'''
        self.angle += self.angle_vel
        wrap(self.pos, self.vel)
#        self.age +=1 # THIS SEEMS TO LENGTHEN THE LIFESPAN, WHY?
        # ALSO, I DON'T NEED ASTEROIDS TO HAVE AN AGE, make a class for asteroids and one for missiles? Meh

    def collision(self, other):
        if dist(self.pos, other.pos)  <  self.radius + other.radius:
            return True
        else:
            return False


def rock_spawner():
    '''timer handler that spawns rocks into a set
    and makes sure the rock doesn't spawn in the same
    position as the ship'''
    global rock_group
    position = [random.randrange(40, 760), random.randrange(40, 560)]
    vel = [pos_or_neg(random.random() * random.randrange(1, 4)),
           pos_or_neg(random.random() * random.randrange(1, 4))] #start slower & increase as game progresses?
    ang  = pos_or_neg(random.randrange(0, 7))
    ang_vel = pos_or_neg(random.random() / 6)
    rock_diameter = 2 * asteroid_info.get_radius()
    ship_diameter = 2 * ship_info.get_radius()

    if len(rock_group) < num_of_asteroids and \
    dist(position, my_ship.pos) >  rock_diameter + ship_diameter + SAFETY:
        rock_group.add(Sprite(position, vel, ang, ang_vel,
                              asteroid_image, asteroid_info))        

def draw(canvas):
    '''updates ~ 60 times a second'''
    global time, started, lives, rock_group, missile_group, score#, my_ship
    # animate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), 
                      nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                      [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, 
                      (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, 
                      (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    # draw and update sprites
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    if started:
        # draw ship
        my_ship.draw(canvas)
        # update ship
        my_ship.update()
    
    # draw score & lives
    canvas.draw_text('SCORE: '+ str(score), (50, 50), 20, 'white', 'monospace')
    draw_lives(canvas)
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
    if group_collide(rock_group, my_ship):
        lives -=1
        print lives
        if lives == 0:
            started = False
            rock_group = set()
            missile_group = set()
            timer.stop()
            soundtrack.pause()
#            my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
            ship_thrust_sound.pause()
#            my_ship.angle_vel = 0
            my_ship.pos = [WIDTH / 2, HEIGHT / 2]
            my_ship.vel = [0, 0]
            my_ship.angle = initial_ship_orientation()
    if group_group_collide(missile_group, rock_group):
        score +=100

def key_press(press):
    '''when a key is pressed down'''
#    if started:###MAKING THESE RELATIVE TO "IF started" FUCKS THEM ALL UP, WHY??
    if press == simplegui.KEY_MAP['left']:
        my_ship.torq('ccw')
    elif press == simplegui.KEY_MAP['right']:
        my_ship.torq('cw')
    elif press == simplegui.KEY_MAP['up']:
        my_ship.rockets(True)
    elif press == simplegui.KEY_MAP['space']:
        if started:
            my_ship.shoot()

def key_release(release):
    '''when a key is released from being pressed down'''
#    if started:
    if release == simplegui.KEY_MAP['left']:
        my_ship.torq('cw')
    elif release == simplegui.KEY_MAP['right']:
        my_ship.torq('ccw')
    elif release == simplegui.KEY_MAP['up']:
        my_ship.rockets(False)

def click(pos):
    global started, lives, score
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        lives = NUM_LIVES
        score = 0
        soundtrack.rewind()
        soundtrack.set_volume(soundtrack_volume)
        soundtrack.play()

def draw_lives(canvas):
    '''draws the lives as mini-ship facing up like
    the original Asteroids - NOTE: based on the
    ImageInfo instance, not the Ship instance'''
#    [canvas.draw_image(ship_image, ship_info.get_center(), ship_info.get_size(),
#                       [60 + life * 25, 70], (20, 20), math.pi * 1.5) \
#                       for life in range(lives) if lives > 0]
    if lives > 0:
        for life in range(lives):
            canvas.draw_image(ship_image, ship_info.get_center(), ship_info.get_size(),
                              [60 + life * 25, 70], (20, 20), math.pi * 1.5)


# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship #Put this in a Class method()?
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], initial_ship_orientation(), 
               ship_image, ship_info)

# register handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000.0, rock_spawner)
frame.set_keydown_handler(key_press)
frame.set_keyup_handler(key_release)
frame.set_mouseclick_handler(click)

# get things rolling
frame.start()


