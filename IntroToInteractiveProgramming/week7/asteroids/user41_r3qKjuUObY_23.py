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
        '''initializes digital image attributes'''
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
ship_image = simplegui.load_image("https://dl.dropbox.com/s/ezp7v5d7ti7dhpg/spaceship.png")
#"http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image(\
"http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("https://dl.dropbox.com/s/gvja7maw8ppthe9/asteroid.png")
#"http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image(\
"http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")
# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound(\
"http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound(\
"http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound(\
"http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound(\
"http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    '''FORWARD: for acceleration in direction of the forward vector'''
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

# Ship class
class Ship:
    '''it spins, it thrusts, it collides, AMAZING!!!'''
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
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
        '''changes the angular velocity in radians'''
        if spin == 'cw': my_ship.angle_vel += my_ship.angle_spin
        elif spin == 'ccw': my_ship.angle_vel -= my_ship.angle_spin

    def rockets(self): #HOW TO GET THRUST RESPONSIVE TO CHANGES IN ROTATION?????????
        if not self.thrust:
            self.image_center[0] -= self.image_size[0]
            self.sound.pause()
        else:
            self.image_center[0] += self.image_size[0]
            self.sound.set_volume(0.3)
            self.sound.rewind()
            self.sound.play()

    def draw(self,canvas):
#        canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        #ANGLE - updates Ship orientation by the
        #        angular velocity (the speed at which Ship spins)
        self.angle += self.angle_vel
        #POSITION FOR TOROIDAL SPACE
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % WIDTH
        #CONSTANT FRICTION
        fric_c = .01
        self.vel[0] *= (1 - fric_c)
        self.vel[1] *= (1 - fric_c)
        #THRUST - ACCELERATION IN DIRECTION OF FWD VECTOR(based on ship orientation)
        fwd_dir = angle_to_vector(self.angle)
        accel_const = 10
        if self.thrust:
            self.vel[0] += fwd_dir[0]# / accel_const
            self.vel[1] += fwd_dir[1]# / accel_const
            print self.vel[0], self.vel[1], self.angle, fwd_dir

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

# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
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
   
    def draw(self, canvas):
#        canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]        

def key_down(key):
    global my_ship
    if simplegui.KEY_MAP['left'] == key:
        my_ship.torq('ccw')
    elif simplegui.KEY_MAP['right'] == key:
        my_ship.torq('cw')
    elif simplegui.KEY_MAP['up'] == key:
        my_ship.thrust = True
        my_ship.rockets()

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
    global time
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
#    a_missile.draw(canvas)

    # update ship and sprites
    my_ship.update()
    a_rock.update()
#    a_missile.update()
            
# timer handler that spawns a rock    
def rock_spawner():
    pass
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [0, 0], 0, .01, asteroid_image, asteroid_info)
#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000.0, rock_spawner)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)

# get things rolling
timer.start()
frame.start()
#print dir(my_ship)