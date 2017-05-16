import simplegui
glob = 5

def keydown_handler(key):
    global glob
    if key == simplegui.KEY_MAP['right']:
        glob *= 2
        print glob
        
def keyup_handler(key):
    global glob
    if key == simplegui.KEY_MAP['right']:
        glob -=3
        print glob
        print

frame = simplegui.create_frame('Testing', 200, 200)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.start()