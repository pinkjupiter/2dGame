from pico2d import *

import game_framework
import main_state
from character import character
from enemy import Enemy2

name = "main_state"

player = None
grass = None
font = None
enemy2 = None
mop = None

class Grass:
    def __init__(self):
        self.image = load_image('resource/grass.png')
        self.background = load_image('resource/stage2.png')

    def draw(self):
        self.image.draw(400, 30)
        self.background.draw(400,400)
def enter():
   global player,grass
   global enemy2,mop
   player = character()
   grass = Grass()
   mop = [Enemy2() for i in range(8)]
def exit():
    global player,grass,mop
    del(player)
    del(grass)
    del(mop)
def pause():
    pass

def resume():
    pass

def handle_events():
   events = get_events()
   global player
   for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN  and event.key == SDLK_ESCAPE:
            game_framework.change_state(main_state)
        else :
            player.handle_event(event)

def update():
    global  mop1
    player.update()
    # mop.update()
    for mop1 in mop:
        mop1.update()

    delay(0.05)
def draw():
    global  mop1
    clear_canvas()
    grass.draw()
    for mop1 in mop:
          mop1.draw()
    player.draw()
    update_canvas()



