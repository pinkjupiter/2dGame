import random
from pico2d import *

__author__ = 'user'

from effect import Effect1
from effect import Effect2
from effect import Effect3

class character:
   global effect1,effect2,effect3
   global effects
   image = None
   hpbar = None
   hpbar2 = None
   frameSize = 2
   jump = True
   gravity = -30
   jumpMove = 0
   LEFT_IDLE, RIGHT_IDLE, LEFT_RUN, RIGHT_RUN,LEFT_JUMP,RIGHT_JUMP,LEFT_ATTACK,RIGHT_ATTACK =7,6,5,4,3,2,1,0

   effect1 = Effect1()
   effect2 = [Effect2() for i in range(3)]
   effect3 = Effect3()
   attack_frame = 0
   global Attack
   Attack = False

   def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 1)
        self.state = self.LEFT_IDLE
        self.jumpPlus = 1
        self.jump = True
        self.gravity = 10
        self.attack_frame = 0
        if character.image == None:
            character.image = load_image('resource/character_sheet.png')


   def handle_event(self, event):
        global effects,effect1,effect3
        global Attack

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_IDLE, self.LEFT_IDLE,self.RIGHT_RUN):
                self.state = self.LEFT_RUN
        elif(event.type, event.key) == (SDL_KEYDOWN,SDLK_RIGHT):
            if self.state in (self.RIGHT_IDLE, self.LEFT_IDLE,self.LEFT_RUN):
                self.state = self.RIGHT_RUN
        # 점프
        elif(event.type, event.key) == (SDL_KEYDOWN,SDLK_SPACE):
                if self.state in (self.RIGHT_IDLE,self.RIGHT_RUN,):
                    self.state = self.RIGHT_JUMP
                    self.jumpMove = 5
                    self.frameSize = 1
                if self.state in (self.LEFT_IDLE,self.LEFT_RUN):
                    self.state = self.LEFT_JUMP
                    self.jumpMove = -5
                    self.frameSize = 1

         # 공격1
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            if self.state in (self.RIGHT_IDLE,self.RIGHT_RUN):
                self.state = self.RIGHT_ATTACK
                self.frameSize = 7
                self.frame = 0
                Attack = True
                self.attack_frame = 0
                count = 0
                effect1.init(self.x,self.y,0)

            if self.state in (self.LEFT_IDLE,self.LEFT_RUN):
                self.state = self.LEFT_ATTACK
                self.frameSize = 74
       # 공격2
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            if self.state in (self.RIGHT_IDLE,self.RIGHT_RUN):
                self.state = self.RIGHT_ATTACK
                self.frameSize = 7
                self.frame = 0
                Attack = True
                self.attack_frame = 0
                count = 0
                for effects in effect2:
                    effects.init(self.x+70+count*150, self.y-15,0)
                    count=count+1
                    print("카운트 %d",count)

            if self.state in (self.LEFT_IDLE,self.LEFT_RUN):
                self.state = self.LEFT_ATTACK
                self.frameSize = 7

        # 공격3
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            if self.state in (self.RIGHT_IDLE,self.RIGHT_RUN):
                self.state = self.RIGHT_ATTACK
                self.frameSize = 7
                self.frame = 0
                Attack = True
                self.attack_frame = 0
                effect3.init(self.x, self.y, 0)
            if self.state in (self.LEFT_IDLE,self.LEFT_RUN):
                self.state = self.LEFT_ATTACK
                self.frameSize = 7



        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_IDLE
                self.frameSize = 2
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_IDLE
                self.frameSize = 2
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_z) :
            if self.state in (self.RIGHT_ATTACK,):
                self.state = self.RIGHT_IDLE
                self.frameSize = 2
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_a) :
            if self.state in (self.RIGHT_ATTACK,):
                self.state = self.RIGHT_IDLE
                self.frameSize = 2
            if self.state in (self.LEFT_ATTACK,):
                self.state = self.LEFT_IDLE
                self.frameSize = 2


   def get_bb(self):
       return self.x - 25, self.y - 50, self.x + 25, self.y + 30

   def update(self):
        global Attack
        global effects,effect1,effect3

        effect1.update()
        effect3.update()
        for effects in effect2:
            if(Attack == True):
                effects.update()
        if self.attack_frame > 15:
            Attack = False
        self.attack_frame = self.attack_frame+1
        self.frame = (self.frame+1) % self.frameSize
        if self.state == self.RIGHT_RUN:
             self.frameSize = 3
             self.x = min(800,self.x+10)
        elif self.state == self.LEFT_RUN:
              self.frameSize = 3
              self.x = max(0,self.x-10)
        elif self.state == self.LEFT_IDLE:
              self.frameSize = 2
        elif self.state == self.RIGHT_IDLE:
              self.frameSize = 2
        #공격
        elif self.state == self.RIGHT_ATTACK:
            pass
            # effect.update()
        #점프
        elif self.state == self.RIGHT_JUMP:
            self.frameSize = 1
            self.x = self.x+self.jumpMove
            if(self.jump):
                self.y = self.y + self.gravity
                self.gravity = self.gravity -2
                if(self.gravity < -10):
                    self.jump = False
                    self.gravity = 10
                    self.state = self.RIGHT_IDLE
            else:
             self.jump = True
             self.frameSize = 1

        elif self.state == self.LEFT_JUMP:
            self.frameSize = 1
            self.x = self.x+self.jumpMove
            if(self.jump):
                self.y = self.y + self.gravity
                self.gravity = self.gravity -2
                if(self.gravity < -10):
                    self.jump = False
                    self.gravity = 10
                    self.state = self.LEFT_IDLE
            else:
             self.jump = True
             self.frameSize = 1
        character.hpbar = load_image("resource/character_hp.png")
        character.hpbar2 = load_image("resource/character_hp_stroke.png")
   def draw(self):
        global Attack
        global effects,effect1,effect3
        self.hpbar2.draw(250,550)
        self.image.clip_draw(self.frame * 150, self.state * 150, 150, 150, self.x, self.y)
        self.hpbar.clip_draw(0,0,250+50,40,250-100+25,550)
        # self.hpbar.draw(250,550)
        draw_rectangle(*self.get_bb())
        for effects in effect2:
            if(self.attack_frame <=15):
                if(Attack == True):
                    effects.draw(self.x,self.y)
        if(Attack == True):
            if(self.attack_frame <=15):
                effect1.draw(self.x,self.y)
                effect3.draw(self.x,self.y)
