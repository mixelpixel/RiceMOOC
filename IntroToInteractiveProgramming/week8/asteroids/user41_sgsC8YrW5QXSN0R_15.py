#- "ROCK STAR" by pdk
#- 160524@2000start
#- yymmdd@????finished
#---------------------------------------------------------------------72
import simplegui, math, random

# globals bindings
WIDTH, HEIGHT = 800, 600
SCREEN_SIZE = (WIDTH, HEIGHT)
score, lives, time = 0, 3, 0
started = False
rock_group = set() #is there a difference with x = ([]) ?
num_of_asteroids = 4
missile_group = set()
num_of_missiles = 5
missile_lifespan = 90

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

#THESE ARE MY IMAGES - PLEASE COMMENT OUT IF THEY DON'T LOAD - THANK YOU!!!!
    splash_info = ImageInfo([200, 150], [400, 300])
    splash_image = simplegui.load_image("https://dl.dropbox.com/s/yaazzsgnraxz5jm/my_splash.png")
    debris_info = ImageInfo([320, 240], [640, 480])
    debris_image = simplegui.load_image("https://dl.dropbox.com/s/uelrcnu4aexo2he/debris.png")
    nebula_info = ImageInfo([400, 300], [800, 600])
    nebula_image = simplegui.load_image("https://dl.dropbox.com/s/h5awm7onocm9v10/space.png")
    ship_info = ImageInfo([45, 45], [90, 90], 35)
    ship_image = simplegui.load_image("https://dl.dropbox.com/s/ezp7v5d7ti7dhpg/spaceship.png")
    missile_info = ImageInfo([5,5], [10, 10], 3, 120)
    missile_image = simplegui.load_image("https://dl.dropbox.com/s/jyly627nc8v1zku/missile.png")
    asteroid_info = ImageInfo([45, 45], [90, 90], 40)
    asteroid_image = simplegui.load_image("https://dl.dropbox.com/s/gvja7maw8ppthe9/asteroid.png")

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
#    explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
#    explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

    # SOUNDS
    # sound assets purchased from sounddogs.com, please do not redistribute
    # alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
    # please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
    # sound assets purchased from sounddogs.com, please do not redistribute
    # .ogg versions of sounds are also available, just replace .mp3 by .ogg
    soundtrack = simplegui.load_sound(\
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
    missile_sound = simplegui.load_sound(\
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
    ship_thrust_sound = simplegui.load_sound(\
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
    explosion_sound = simplegui.load_sound(\
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
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
    sign = random.choice([False, True]) #sign = random.choice([0,1])
    if sign: return num                 #works for 'false or true' also
    else: return -num

def wrap(position, vector):
    """Moves the position by the given vector in 2D toroidal space."""
    #REPLACES THIS:
#        self.pos[0] = (self.pos[0] + self.vel[0]) % WI{DTH
#        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
    for d in range(2):
        position[d] = (position[d] + vector[d]) % SCREEN_SIZE[d]

def process_sprite_group(sprite_group, canvas):
    '''handles drawing and updates for any group of Sprites'''
    global missile_group
    if started:
        timer.start()
        for sprite in sprite_group:
            sprite.draw(canvas)
        for sprite in sprite_group:
            sprite.update()
    for missile in list(missile_group):
        missile.age +=1
        if missile.age > missile_lifespan:
            missile_group.remove(missile)

def group_collide(group, other_object):
    global lives
    for sprite in list(group):
        if sprite.collision(other_object):
            group.remove(sprite)
            lives -=1
            print 'lives = ' + str(lives)

def group_group_collide(group1, group2):
    for m in group1:
        group_collide(group2, m)
#    for i in group1:
#        collidewith j in group2?



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

        global missile_group
        fwd = angle_to_vector(self.angle)
        msl_pos = [self.pos[0] + self.radius * fwd[0],
                   self.pos[1] + self.radius * fwd[1]]
        msl_vel = [self.vel[0] + 10 * fwd[0], ###WHY 10? IS THERE A BETTER WAY TO
                   self.vel[1] + 10 * fwd[1]] ###HANDLE THIS SCALING FACTOR?
        if len(missile_group) < num_of_missiles:
            missile_group.add(Sprite(msl_pos, msl_vel, 0, .1,
                                     missile_image, missile_info, missile_sound))
            for missile in missile_group:
                print len(missile_group), missile.__str__()
            print

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
        self.vel[0] *= (1 - fric_c)
        self.vel[1] *= (1 - fric_c)

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
        if sound:
            sound.rewind()
            sound.play()
            sound.set_volume(.2)

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

    def collision(self, other_object):
        self.other_object = other_object
        if dist(self.pos, other_object.pos) < self.radius + other_object.radius:
            return True
        else:
            return False


def rock_spawner():
    '''timer handler that spawns rocks into a set'''
    global rock_group
    position = [random.randrange(40, 760), random.randrange(40, 560)]
    vel = [pos_or_neg(random.random() * random.randrange(1, 4)),
           pos_or_neg(random.random() * random.randrange(1, 4))]
    ang  = pos_or_neg(random.randrange(0, 7))
    ang_vel = pos_or_neg(random.random() / 6)
    total_rocks = 8
    if len(rock_group) < num_of_asteroids:
        rock_group.add(Sprite(position, vel, ang, ang_vel,
                              asteroid_image, asteroid_info))
        for rock in rock_group:
            print len(rock_group), rock.__str__()
        print


def draw(canvas):
    '''updates ~ 60 times a second'''

    global time, score, started
    
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

    # draw ship
    my_ship.draw(canvas)

    # update ship
    my_ship.update()
    
    # draw score & lives
    canvas.draw_text('SCORE: '+ str(score), (50, 50), 
                     20, 'white', 'monospace')
    draw_lives(canvas)
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())

    group_collide(rock_group, my_ship)
    group_group_collide(missile_group, rock_group)

def key_press(press):
    '''when a key is pressed down'''
    if press == simplegui.KEY_MAP['left']: #BETTER TO MAKE AN IF/ELIF/ELIF... CHAIN?
        my_ship.torq('ccw')
    if press == simplegui.KEY_MAP['right']:
        my_ship.torq('cw')
    if press == simplegui.KEY_MAP['up']:
        my_ship.rockets(True)
    if press == simplegui.KEY_MAP['space']:
        if started:
            my_ship.shoot() #EXPAND ON THIS SO GAME STARTS OVER CORRECTLY

def key_release(release):
    '''when a key is released from being pressed down'''
    if release == simplegui.KEY_MAP['left']: #BIG O NOTATION DIFFERENCE????
        my_ship.torq('cw')
    if release == simplegui.KEY_MAP['right']:
        my_ship.torq('ccw')
    if release == simplegui.KEY_MAP['up']:
        my_ship.rockets(False)

def click(pos):
    global started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True

def draw_lives(canvas): #This needs improving
    '''this could be written MUCH better'''
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
    elif lives == 1:
        canvas.draw_image(my_ship.image, [45, 45], my_ship.image_size, 
                          [60, 70], (20, 20), math.pi * 1.5)



        

#THESE BUTTON FUNCTIONS DIDN'T WORK AS I'D HOPED
#def coursera_grfx():
#    global debris_image, nebula_image, ship_image, missile_image, asterois_image
#    debris_image = simplegui.load_image(\
#    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")
#    nebula_image = simplegui.load_image(\
#    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")
#    ship_image = simplegui.load_image(\
#    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
#    missile_image = simplegui.load_image(\
#    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
#    asteroid_image = simplegui.load_image(\
#    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
#
#def my_awesome_grfx():
#    global debris_image, nebula_image, ship_image, missile_image, asterois_image
#    debris_image = simplegui.load_image("https://dl.dropbox.com/s/uelrcnu4aexo2he/debris.png")
#    nebula_image = simplegui.load_image("https://dl.dropbox.com/s/h5awm7onocm9v10/space.png")
#    ship_image = simplegui.load_image("https://dl.dropbox.com/s/ezp7v5d7ti7dhpg/spaceship.png")
#    missile_image = simplegui.load_image("https://dl.dropbox.com/s/jyly627nc8v1zku/missile.png")
#    asteroid_image = simplegui.load_image("https://dl.dropbox.com/s/gvja7maw8ppthe9/asteroid.png")

def score_plus():
    global score
    score +=100
def yer_dead():
    global lives
    lives -=1



# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, 
               ship_image, ship_info)


# register handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000.0, rock_spawner)
frame.set_keydown_handler(key_press)
frame.set_keyup_handler(key_release)
#button1 = frame.add_button('Coursera Graphics', coursera_grfx)
#button2 = frame.add_button('My Awesome Graphics', coursera_grfx)
add_to_score = frame.add_button('Add to Score', score_plus)
lives_lost = frame.add_button('Decrease Lives', yer_dead)
frame.set_mouseclick_handler(click)

# get things rolling
#timer.start()
frame.start()


