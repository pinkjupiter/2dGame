from pico2d import *

import game_framework
import title_state

import stage1
import stage2
import stage3
import stage4
name = "main_state"

stage = None

class Stage:
    def __init__(self):
        self.stage1logo = load_image('resource/stage1logo.png')
        self.stage2logo = load_image('resource/stage2logo.png')
        self.stage3logo = load_image('resource/stage3logo.png')
        self.stageBackground = load_image('resource/stagebackground.png')
    def draw(self):
        self.stageBackground.draw(400,300)
        self.stage1logo.draw(200,450)
        self.stage2logo.draw(400,450)
        self.stage3logo.draw(600,450)


def enter():
    global stage
    stage = Stage()
   # global player,grass
   # global enemy1,mop
   # player = character()
   # grass = Grass()
   # enemy1 = Enemy()
   # mop = [Enemy() for i in range(10)]
def exit():
    pass
    # global player,grass,enemy1
    # del(player)
    # del(grass)
    # del(enemy1)
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
        elif event.type == SDL_KEYDOWN  and event.key == SDLK_1:
            game_framework.change_state(stage1)
        elif event.type == SDL_KEYDOWN  and event.key == SDLK_2:
            game_framework.change_state(stage2)
        elif event.type == SDL_KEYDOWN  and event.key == SDLK_3:
            game_framework.change_state(stage3)
        elif event.type == SDL_KEYDOWN  and event.key == SDLK_4:
            game_framework.change_state(stage4)
        # else :
        #     player.handle_event(event)

def update():
    # global  mop1
    # player.update()
    # enemy1.update()
    # # mop.update()
    # for mop1 in mop:
    #     mop1.update()

    delay(0.05)
def draw():
    global  mop1
    clear_canvas()
    stage.draw()
    # grass.draw()
    # enemy1.draw()
    # for mop1 in mop:
    #       mop1.draw()
    # player.draw()
    update_canvas()



