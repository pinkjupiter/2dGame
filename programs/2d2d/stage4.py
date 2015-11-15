from pico2d import *

import game_framework
import main_state
from character import character
from enemy import Boss

name = "main_state"

player = None
grass = None
font = None
boss  = None

class Grass:
    def __init__(self):
        self.image = load_image('resource/grass.png')
        self.background = load_image('resource/stage4.png')

    def draw(self):
        self.image.draw(400, 30)
        self.background.draw(400,300)
def enter():
   global player,grass
   global enemy1,mop
   global boss
   player = character()
   grass = Grass()
   boss = Boss()

def exit():
    global player,grass,enemy1,boss
    del(player)
    del(grass)
    del(boss)
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
    player.update()
    # mop.update()
    boss.update()

    delay(0.05)
def draw():
    global  boss
    clear_canvas()
    grass.draw()
    # for mop1 in mop:
    #       mop1.draw()
    player.draw()
    boss.draw()
    update_canvas()



