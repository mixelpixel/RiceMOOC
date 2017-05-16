import simplegui
position = [10, 20]
#vect = [3, 0.7]
vect = [0, 0]
print position, vect
##count = 0

def vector():
    position[0] += vect[0]
    position[1] += vect[1]

def draw_handler(canvas):
    canvas.draw_circle(position, 5, 1, 'Green')
    canvas.draw_polygon([[50, 50], [180, 50], [180, 140], [50, 140]], 1, 'Red')
#    vector()
#    print position
    position[0] += vect[0]
    position[1] += vect[1]

    
##def button_handler():
##    global count
##    count +=1
##    vector()
##    print position, count

###def keydown_handler(key):
###    if key == simplegui.KEY_MAP['right']:
###        vector()
###        print position

def keydown_handler(key):
    if key == simplegui.KEY_MAP['right']:
        vect[0] = 3
        vect[1] = 0.7
        print position

def keyup_handler(key):
    if key == simplegui.KEY_MAP['right']:
        vect[0] = 0
        vect[1] = 0

frame = simplegui.create_frame('Testing', 200, 200)
frame.set_draw_handler(draw_handler)
##frame.add_button('vector', button_handler, 100)
###frame.set_keydown_handler(keydown_handler)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.start()