import random
import json
import os

from pico2d import *

import game_framework
import title_state
from character import character

name = "main_state"

player = None
grass = None
font = None

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)
def enter():
   global player,grass
   global hero
   player = character()
   grass = Grass()

def exit():
    global player,grass
    del(player)
    del(grass)

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
            game_framework.change_state(title_state)
        else :
            player.handle_event(event)

def update():
    player.update()

def draw():
    clear_canvas()
    grass.draw()
    player.draw()
    update_canvas()





