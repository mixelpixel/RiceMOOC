# Sprite class emo
import simplegui
import math

# helper class to organize image information
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

# load ship image
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("https://www.dropbox.com/s/gvja7maw8ppthe9/asteroid.png")

#spaceship_info = ImageInfo([45, 45], [180, 90] , 40)
#spaceship_image = simplegui.load_image("https://www.dropbox.com/s/ezp7v5d7ti7dhpg/spaceship.png")

# Sprite class
class Sprite():
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
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
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

           
def draw(canvas):

    # draw ship and sprites
    a_rock.draw(canvas)
#    a_spaceship.draw(canvas)
    
    # update ship and sprites
    a_rock.update()
#    a_spaceship.update()
                
# initialize frame
frame = simplegui.create_frame("Sprite demo", 800, 600)

# initialize ship and two sprites
a_rock = Sprite([400, 300], [0.3, 0.4], 0, 0.1, asteroid_image, asteroid_info)
#a_spaceship = Sprite([100,100], [0.2, 0.3], 0, 0.01, spaceship_image, spaceship_info)

# register handlers
frame.set_draw_handler(draw)

# get things rolling
frame.start()
