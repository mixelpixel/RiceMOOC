#- "ASTEROIDS" by pdk
#- 160516@2100start
#- 160521@0300finished
#---------------------------------------------------------------------72

#- import modules
import simplegui, math, random

# globals bindings
WIDTH, HEIGHT = 800, 600
score, lives, time = 0, 3, 0

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

def declarations():
    '''I zipped all these up into a function
    because they are really ugly to look at
    and now I can collapse them as I work :D'''
    global debris_info, debris_image, \
    nebula_info, nebula_image, \
    splash_info, splash_image, \
    ship_info, ship_image, \
    missile_info, missile_image, \
    asteroid_info, asteroid_image, \
    explosion_info, explosion_image, \
    soundtrack, missile_sound, ship_thrust_sound, explosion_sound
    # IMAGES
    # art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    # debris images: debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
    #                debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
    debris_info = ImageInfo([320, 240], [640, 480])
    debris_image = simplegui.load_image("https://dl.dropbox.com/s/uelrcnu4aexo2he/debris.png")
    #"http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")
    # nebula images - nebula_brown.png, nebula_blue.png
    nebula_info = ImageInfo([400, 300], [800, 600])
    nebula_image = simplegui.load_image("https://dl.dropbox.com/s/h5awm7onocm9v10/space.png")
    #"http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")
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
    missile_image = simplegui.load_image("https://dl.dropbox.com/s/jyly627nc8v1zku/missile.png")
    #"http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
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



# helper functions
def angle_to_vector(ang):
    '''FORWARD: for acceleration in direction of the forward vector
    converts the radian angle to a vector: REVIEW TRIGONOMETRY.
    Returns a vector consisting in 2 real numbers between -1 and 1'''
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    '''not in use'''
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

def pos_or_neg(num):
    '''returns a POSitive OR NEGative numeric value'''
    #can also be re-written with random.uniform(-1, 1)
    #but the way I've implemented it with the rock_spawner
    #it nicely avoids zero values
    sign = random.choice([False, True]) #sign = random.choice([0,1])
    if sign: return num                 #works for 'false or true' also
    else: return -num



# Ship class
class Ship:
    '''it spins, it thrusts, it shoots, it's AMAZING!!!
    and there's more to come in the next installment :)'''
    def __init__(self, pos, vel, angle, image, info):
        '''initializes attributes for the Ship class instances'''
        self.pos = [pos[0],pos[1]] #Ship position
        self.vel = [vel[0],vel[1]] #Ship velocity
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0 #Radians, not degrees
        self.angle_spin = .08 #change in angular velocity
        self.image = image
        self.image_center = info.get_center()
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
            self.sound.set_volume(0.3)
            self.sound.rewind()
            self.sound.play()
        else: #when firing stops, return to:
            self.image_center[0] -= self.image_size[0]
            self.sound.pause()

    def shoot(self):
        '''method to spawn missiles and handle missile attributes
        for position, velocity and forward acceleration.
        "msl" = "missile"'''
        global a_missile
        fwd = angle_to_vector(self.angle)
        msl_pos = [self.pos[0] + self.radius * fwd[0],
                   self.pos[1] + self.radius * fwd[1]]
        msl_vel = [self.vel[0] + 10 * fwd[0], ###WHY 10? IS THERE A BETTER WAY TO
                   self.vel[1] + 10 * fwd[1]] ###HANDLE THIS SCALING FACTOR?
        a_missile = Sprite(msl_pos, msl_vel, 0, .1,
                           missile_image, missile_info, missile_sound)

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
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        #CONSTANT FRICTION
        fric_c = .01 #BETTER WAY TO HANDLE THIS FRICASSEE FACTOR?????
        self.vel[0] *= (1 - fric_c)
        self.vel[1] *= (1 - fric_c)
        #THRUST - ACCELERATION IN DIRECTION OF FWD VECTOR
        #based on ship orientation
        fwd_dir = angle_to_vector(self.angle)
        accel_const = 10
        if self.thrust:
            self.vel[0] += fwd_dir[0] / accel_const
            self.vel[1] += fwd_dir[1] / accel_const

# Sprite class
class Sprite:
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
        if sound:
            sound.rewind()
            sound.play()
            sound.set_volume(.2)

    def draw(self, canvas):
        '''method to draw the Sprite instances'''
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)

    def update(self):
        '''method to update attributes of Sprite class instances'''
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT



def draw(canvas):
    global time, score
    
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

    # draw ship and sprites
    a_rock.draw(canvas)
    my_ship.draw(canvas)
    a_missile.draw(canvas)

    # update ship and sprites
    a_rock.update()
    my_ship.update()
    a_missile.update()
    
    # score & lives
    canvas.draw_text('SCORE: '+ str(score), (50, 50), 
                     20, 'white', 'monospace')
    draw_lives(canvas)


def key_press(press):
    global my_ship
    if press == simplegui.KEY_MAP['left']: #BETTER TO MAKE AN IF/ELIF/ELIF... CHAIN?
        my_ship.torq('ccw')
    if press == simplegui.KEY_MAP['right']:
        my_ship.torq('cw')
    if press == simplegui.KEY_MAP['up']:
        my_ship.rockets(True)
    if press == simplegui.KEY_MAP['space']:
        my_ship.shoot()

def key_release(release):
    global my_ship
    if release == simplegui.KEY_MAP['left']: #BIG O NOTATION DIFFERENCE????
        my_ship.torq('cw')
    if release == simplegui.KEY_MAP['right']:
        my_ship.torq('ccw')
    if release == simplegui.KEY_MAP['up']:
        my_ship.rockets(False)

def draw_lives(canvas): #This needs improving
    '''this could be MUCH better'''
    if lives == 3:
        canvas.draw_image(my_ship.image, [45, 45], my_ship.image_size, 
                          [60, 70], (20, 20), math.pi * 1.5)
        canvas.draw_image(my_ship.image, [45, 45], my_ship.image_size, 
                          [85, 70], (20, 20), math.pi * 1.5)
        canvas.draw_image(my_ship.image, [45, 45], my_ship.image_size, 
                          [110, 70], (20, 20), math.pi * 1.5)
    elif lives == 2:
        canvas.draw_image(my_ship.image, [45, 45], my_ship.image_size, 
                          [60, 70], (20, 20), math.pi * 1.5)
        canvas.draw_image(my_ship.image, [45, 45], my_ship.image_size, 
                          [85, 70], (20, 20), math.pi * 1.5)
    else:
        canvas.draw_image(my_ship.image, [45, 45], my_ship.image_size, 
                          [60, 70], (20, 20), math.pi * 1.5)

def rock_spawner():
    '''timer handler that spawns a rock'''
    global a_rock
    position = [random.randrange(40, 760), random.randrange(40, 560)]
    vel = [pos_or_neg(random.random() * random.randrange(1, 4)),
           pos_or_neg(random.random() * random.randrange(1, 4))]
    ang  = pos_or_neg(random.randrange(0, 7))
    ang_vel = pos_or_neg(random.random() / 6)
    a_rock = Sprite(position, vel, ang, ang_vel, asteroid_image, 
                    asteroid_info)

def button_handler1():
    global debris_image, nebula_image, ship_image, missile_image, asteroid_image
    debris_image, nebula_image, ship_image, missile_image, asteroid_image\
    = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png"),
    simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png"),
    simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png"),
    simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png"),
    simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")


def button_handler2():
    global debris_image, nebula_image, ship_image, missile_image, asteroid_image
    debris_image, nebula_image, ship_image, missile_image, asteroid_image\
    = simplegui.load_image("https://dl.dropbox.com/s/uelrcnu4aexo2he/debris.png"),
    simplegui.load_image("https://dl.dropbox.com/s/h5awm7onocm9v10/space.png"),
    simplegui.load_image("https://dl.dropbox.com/s/ezp7v5d7ti7dhpg/spaceship.png"),
    simplegui.load_image("https://dl.dropbox.com/s/jyly627nc8v1zku/missile.png"),
    simplegui.load_image("https://dl.dropbox.com/s/gvja7maw8ppthe9/asteroid.png")


# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, 
               ship_image, ship_info)
a_missile = Sprite([750, 550], [-1, -1], 0, math.pi/120,
                   missile_image, missile_info, missile_sound)
a_rock = Sprite([random.randrange(WIDTH), random.randrange(HEIGHT)],
                [pos_or_neg(random.random() * random.randrange(1, 4)),
                 pos_or_neg(random.random() * random.randrange(1, 4))],
                0, pos_or_neg(random.random() / 6),asteroid_image, 
                asteroid_info)

# register handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000.0, rock_spawner)
frame.set_keydown_handler(key_press)
frame.set_keyup_handler(key_release)
button1 = frame.add_button('Coursera GRFX', button_handler1)
button2 = frame.add_button('Silly GRFX', button_handler2)

# get things rolling
timer.start()
frame.start()




####TO DO: THINK ABOUT THIS AND SEE HOW IT CAN APPLY
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