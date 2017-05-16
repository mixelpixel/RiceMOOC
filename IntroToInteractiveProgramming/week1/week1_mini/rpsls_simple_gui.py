import simplegui, random

# Musica
class Music:
    
    def __init__(self):
        self.tracks = []
        self.current_track = None
        self.volume = 0.03
        self.playing = False
        
    def add_tracks(self, track_list):
        for i in range(0, len(track_list)):
            self.tracks.append(track_list[i])
        
    def play_track(self, track = 0):
        if self.playing == False:
            self.current_track = simplegui.load_sound(self.tracks[track])
            self.current_track.set_volume(self.volume)
            self.current_track.play()
            self.playing = True
        
    def pause_track(self):
        self.current_track.pause()        
        
    def volume_up(self):
        if self.current_track:
            if self.volume < 1:
                self.volume = self.volume + 0.01
                self.current_track.set_volume(self.volume)
    
    def volume_down(self):
        if self.current_track:
            if self.volume > 0.01:
                self.volume = self.volume - 0.01
                self.current_track.set_volume(self.volume)

# Set up background music        
BGM = Music()
BGM.add_tracks([
                'https://www.dropbox.com/s/u0lvdtae26ufcv1/Final%20Fantasy%20VII%20Battle%20Theme%20Acapella.mp3?raw=1'
              ])    





## Game Functions


# Select the icon that was clicked
def icon_clicked(mouse, icon):
    if (mouse[0] > icon['x'][0] and mouse[0] < icon['x'][1] and
        mouse[1] > icon['y'][0] and mouse[1] < icon['y'][1]):
        RPSLS.active_icon = icon 
        
# Check if clicked position is inside icon
def mouse_handler(position):
    if RPSLS.round_refresh == False:
        for i in range(0, len(RPSLS.data)):
            icon_clicked(position, RPSLS.data[i])

# Show selected icon
def flashing_icon():
    if RPSLS.icon_pulse == 3:
        RPSLS.switch = True
    if RPSLS.icon_pulse < 0.1:
        RPSLS.switch = False
    if RPSLS.switch:
        RPSLS.icon_pulse = RPSLS.icon_pulse - 0.1
    else:
        RPSLS.icon_pulse = RPSLS.icon_pulse + 0.1
        
    return RPSLS.icon_pulse


def start_round():
    if RPSLS.round_refresh == False:
        if RPSLS.active_icon:
            RPSLS.cpu = RPSLS.data[random.randrange(0, 5)]
            RPSLS.timer.start()
            RPSLS.round_refresh = True

# Round resets after 2 seconds
def reset_round():
    RPSLS.active_icon = None
    RPSLS.cpu = None
    RPSLS.timer.stop()
    RPSLS.round_refresh = False
        
    

# Show loser
def marked_out(canvas, icon):
    canvas.draw_line((icon['x'][0], icon['y'][0]),
                     (icon['x'][1], icon['y'][1]), 3, 'Red')
              

# Loop       
def draw(canvas):
    canvas.draw_image(RPSLS.image, (350,350), (700, 700), (100, 100), (200, 200))
    if RPSLS.active_icon:
        x = flashing_icon()
        canvas.draw_circle((RPSLS.active_icon['circle'][0], 
                            RPSLS.active_icon['circle'][1]),
                            31, x, 'hsla(60, 90%, 50%, 1)')
    if RPSLS.cpu:
        canvas.draw_circle((RPSLS.cpu['circle'][0], 
                            RPSLS.cpu['circle'][1]),
                            31, x, 'hsla(250, 90%, 50%, 1)')
        if RPSLS.cpu == RPSLS.active_icon:
            canvas.draw_text('DRAW', (50, 100), 30, 'hsla(320, 0%, 0%, 1)')
        else:
            if (RPSLS.cpu['defeat'][0] == RPSLS.active_icon['id'] or
                RPSLS.cpu['defeat'][1] == RPSLS.active_icon['id']):
                
                marked_out(canvas, RPSLS.cpu)
                canvas.draw_text('YOU WIN', (50, 100), 30, 'hsla(320, 0%, 0%, 1)')
            else:
                marked_out(canvas, RPSLS.active_icon)
                canvas.draw_text('YOU LOSE', (50, 100), 30, 'hsla(320, 0%, 0%, 1)')
    
        
        

data = [ 
           {'id': 'rock',
            'x': (74, 126),
            'y': (17, 65),
            'circle': (100, 44),
            'defeat': ('paper', 'spock')},
    
            {'id': 'spock',
            'x': (15, 63),
            'y': (62, 112),
            'circle': (41, 88),
            'defeat': ('paper', 'lizard')},    
        
            {'id': 'paper',
            'x': (132, 184),
            'y': (62, 104),
            'circle': (158, 88),
            'defeat': ('lizard', 'scissors')},
    
            {'id': 'lizard',
            'x': (36, 88),
            'y': (132, 184),
            'circle': (62, 158),
            'defeat': ('rock', 'scissors')},
    
            {'id': 'scissors',
            'x': (111, 163),
            'y': (132, 184),
            'circle': (137, 158),
            'defeat': ('rock', 'spock')}
       ]

# Lazy
class Game:
    def __init__(self):
        self.data = data
        self.active_icon = None
        self.icon_pulse = 3
        self.icon_switch = True
        self.cpu = None
        self.round_refresh = False
        self.timer = simplegui.create_timer(2000, reset_round)
        self.image = simplegui.load_image('https://www.dropbox.com/s/cn0upc2pz5x1mfl/b597_rock_papaer_scissors_lizard_spock_dd.jpg?raw=1')
            
    def create_window(self):
        self.window = simplegui.create_frame('Arena', 200, 200)
        self.window.set_canvas_background('White')
        self.window.add_button('Get in the zone', BGM.play_track, 110)
        self.window.add_button('+', BGM.volume_up, 110)
        self.window.add_button('-', BGM.volume_down, 110)
        self.window.add_button('Start Round', start_round, 110)
        self.window.add_label('')
        self.window.add_label('Choose your weapon.')
        self.window.add_label('Start Round.')
        self.window.set_mouseclick_handler(mouse_handler)
        self.window.set_draw_handler(draw)
        

# Round 1... FIGHT!
RPSLS = Game()
RPSLS.create_window()       
RPSLS.window.start()
     
 




