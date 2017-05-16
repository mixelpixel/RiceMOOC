#- "ASTEROIDS", pdk, started: 5/16/16 @ 9pm, finished m/d/y @ ??:??
#---------------------------------------------------------------------72
#- import modules
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0

class ImageInfo:
    '''A Classy way of handling imagery information'''
    def __init__(self, center, size, radius = 0,
                 lifespan = None, animated = False):
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
        '''returns the images center (width, height) from the referenced grfx'''
        return self.center

    def get_size(self):
        '''returns the images size dimensions (width, height) from the referenced grfx'''
        return self.size

    def get_radius(self):
        '''returns the effective radius of the image
        for calculating Sprite collisions'''
        return self.radius

    def get_lifespan(self):
        '''returns the images lifespan'''
        return self.lifespan

    def get_animated(self):
        '''returns the animation status of an image stack/array'''
        return self.animated

def declarations():
    global debris_info, debris_image, nebula_info, nebula_image, \
    splash_info, splash_image, ship_info, ship_image, missile_info, missile_image, \
    asteroid_info, asteroid_image, explosion_info, explosion_image, \
    soundtrack, missile_sound, ship_thrust_sound, explosion_sound
    # IMAGES
    # art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    # debris images: debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
    #                debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
    debris_info = ImageInfo([320, 240], [640, 480])
    debris_image = simplegui.load_image(\
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")
    # nebula images - nebula_brown.png, nebula_blue.png
    nebula_info = ImageInfo([400, 300], [800, 600])
    nebula_image = simplegui.load_image(\
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")
    # splash image
    splash_info = ImageInfo([200, 150], [400, 300])
    splash_image = simplegui.load_image("\
    http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")
    # ship image
    ship_info = ImageInfo([45, 45], [90, 90], 35)
    ship_image = simplegui.load_image("https://dl.dropbox.com/s/ezp7v5d7ti7dhpg/spaceship.png") #PDK
    #"http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
    # missile image - shot1.png, shot2.png, shot3.png
    missile_info = ImageInfo([5,5], [10, 10], 3, 120)
    missile_image = simplegui.load_image(\
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
    # asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
    asteroid_info = ImageInfo([45, 45], [90, 90], 40)
    asteroid_image = simplegui.load_image("https://dl.dropbox.com/s/gvja7maw8ppthe9/asteroid.png") #PDK
    #"http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
    # animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
    explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
    explosion_image = simplegui.load_image(\
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

    # SOUNDS
    # sound assets purchased from sounddogs.com, please do not redistribute
    # alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
    # please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
    #soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")
    soundtrack = simplegui.load_sound(\
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
    missile_sound = simplegui.load_sound(\
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
    #missile_sound.set_volume(.5)
    ship_thrust_sound = simplegui.load_sound(\
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
    explosion_sound = simplegui.load_sound(\
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
declarations()

# helper functions to handle transformations
def angle_to_vector(ang):
    '''FORWARD: for acceleration in direction of the forward vector'''
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    '''not in use'''
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

def pos_or_neg(num):
    '''returns a positive or negative numeric value'''
    r = random.choice([False, True])
#    r = random.choice([0,1]) #works for 'false or true' as well
    if r: return -num
    else: return num

# Ship class
class Ship:
    '''it spins, it thrusts, it shoots, AMAZING!!!
    and more to come in the next installment :)'''
    def __init__(self, pos, vel, angle, image, info):
        '''initializes attributes for the Ship class instances'''
        self.pos = [pos[0],pos[1]] #Ship position
        self.vel = [vel[0],vel[1]] #Ship velocity
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0 #Radians, not degrees
        self.angle_spin = .09 #change in angular velocity
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.sound = ship_thrust_sound

    def torq(self, spin):
        '''method to change the angular velocity in radians'''
        if spin == 'cw': my_ship.angle_vel += my_ship.angle_spin
        elif spin == 'ccw': my_ship.angle_vel -= my_ship.angle_spin

    def rockets(self):
        '''method to handle rocket imagery and sounds'''
        if not self.thrust:
            self.image_center[0] -= self.image_size[0]
            self.sound.pause()
        else:
            self.image_center[0] += self.image_size[0]
            self.sound.set_volume(0.3)
            self.sound.rewind()
            self.sound.play()

    def shoot(self):
        '''method to spawn handle missiles and handle
        missile attributes for position, velocity and
        forward acceleration'''
        global a_missile
        fwd = angle_to_vector(self.angle)
        msl_pos = [self.pos[0] + self.radius * fwd[0],
                   self.pos[1] + self.radius * fwd[1]]
        msl_vel = [self.vel[0] + 10 * fwd[0], self.vel[1] + 10 * fwd[1]]
        a_missile = Sprite(msl_pos, msl_vel, 0, 0,
                           missile_image, missile_info, missile_sound)

    def draw(self,canvas):
        '''method to draw the Ship image'''
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        '''method to handle Ship attribute updates'''
        #ANGLE - updates Ship orientation by the
        #        angular velocity (the speed at which Ship spins)
        self.angle += self.angle_vel
        #POSITION FOR TOROIDAL SPACE
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        #CONSTANT FRICTION
        fric_c = .01
        self.vel[0] *= (1 - fric_c)
        self.vel[1] *= (1 - fric_c)
        #THRUST - ACCELERATION IN DIRECTION OF FWD VECTOR(based on ship orientation)
        fwd_dir = angle_to_vector(self.angle)
        accel_const = 10
        if self.thrust:
            self.vel[0] += fwd_dir[0] / accel_const
            self.vel[1] += fwd_dir[1] / accel_const

# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        '''initializes attributes for the Sprite instances'''
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel #Radians, not degrees!!! ~(2*pi = 360deg)
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
            sound.set_volume(.2)

    def draw(self, canvas):
        '''method to draw the Sprite instances'''
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        '''method to update attributes of Sprite class instances'''
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

def key_down(key):
    global my_ship
    if simplegui.KEY_MAP['left'] == key:
        my_ship.torq('ccw')
    elif simplegui.KEY_MAP['right'] == key:
        my_ship.torq('cw')
    elif simplegui.KEY_MAP['up'] == key:
        my_ship.thrust = True
        my_ship.rockets()
    elif simplegui.KEY_MAP['space'] == key:
        my_ship.shoot()

def key_up(key):
    global my_ship
    if simplegui.KEY_MAP['left'] == key:
        my_ship.torq('cw')
    elif simplegui.KEY_MAP['right'] == key:
        my_ship.torq('ccw')
    elif simplegui.KEY_MAP['up'] == key:
        my_ship.thrust = False
        my_ship.rockets()

def draw(canvas):
    global time, score
    
    # animate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    a_rock.draw(canvas)
    my_ship.draw(canvas)
    a_missile.draw(canvas)

    # update ship and sprites
    a_rock.update()
    my_ship.update()
    a_missile.update()
    
    # score & lives
    canvas.draw_text('SCORE: '+ str(score), (50, 50), 20, 'white', 'monospace')
    def draw_lives():
        '''this could be better'''
        if lives == 3:
            canvas.draw_image(my_ship.image, [45, 45], my_ship.image_size, [60, 70], (20, 20), math.pi * 1.5)
            canvas.draw_image(my_ship.image, [45, 45], my_ship.image_size, [85, 70], (20, 20), math.pi * 1.5)
            canvas.draw_image(my_ship.image, [45, 45], my_ship.image_size, [110, 70], (20, 20), math.pi * 1.5)
        elif lives == 2:
            canvas.draw_image(my_ship.image, [45, 45], my_ship.image_size, [60, 70], (20, 20), math.pi * 1.5)
            canvas.draw_image(my_ship.image, [45, 45], my_ship.image_size, [85, 70], (20, 20), math.pi * 1.5)
        else:
            canvas.draw_image(my_ship.image, [45, 45], my_ship.image_size, [60, 70], (20, 20), math.pi * 1.5)
    draw_lives()
            
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    position = [random.randrange(40, 760), random.randrange(40, 560)]
    vel = [pos_or_neg(random.random() * random.randrange(1, 4)),
           pos_or_neg(random.random() * random.randrange(1, 4))]
    ang  = pos_or_neg(random.randrange(0, 7))
    ang_vel = pos_or_neg(random.random() / 6)
    a_rock = Sprite(position, vel, ang, ang_vel, asteroid_image, asteroid_info)

# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)

a_missile = Sprite([750, 550], [-1, -1], 0, math.pi/120,
                   missile_image, missile_info, missile_sound)

a_rock = Sprite([random.randrange(WIDTH), random.randrange(HEIGHT)],
                [pos_or_neg(random.random() * random.randrange(1, 4)),
                 pos_or_neg(random.random() * random.randrange(1, 4))],
                0, pos_or_neg(random.random() / 6),asteroid_image, asteroid_info)

# register handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000.0, rock_spawner)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)

# get things rolling
timer.start()
frame.start()




######from the test
######def move_dimension(dimension, position, vector):
######    """Moves the position component by the given vector component in 1D toroidal space."""
######    position[dimension] = (position[dimension] + vector[dimension]) % SCREEN_SIZE[dimension]
######
######def move(position, vector):
######    """Moves the position by the given vector in 2D toroidal space."""
######    move_dimension(0, position, vector)
######    move_dimension(1, position, vector)
################OR THIS:
#########NUM_DIMENSIONS = 2
#########def move(position, vector):
#########    """Moves the position by the given vector in 2D toroidal space."""
#########    for d in range(NUM_DIMENSIONS):
#########        position[d] = (position[d] + vector[d]) % SCREEN_SIZE[d]
#################OR THIS:
#################def move(position, vector):
#################    """Moves the position by the given vector in 2D toroidal space."""
#################    position[0] = (position[0] + vector[0]) % SCREEN_SIZE[0]
#################    position[1] = (position[1] + vector[1]) % SCREEN_SIZE[1]