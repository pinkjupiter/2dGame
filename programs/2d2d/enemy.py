import random
from pico2d import *

__author__ = 'user'


class Enemy:
   image = None
   frameSize = 6
   LEFT_IDLE, RIGHT_IDLE, LEFT_RUN, RIGHT_RUN,LEFT_HIT,RIGHT_HIT,LEFT_DIE,RIGHT_DIE =7,6,5,4,3,2,1,0

   def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.startx = self.x
        self.frame = random.randint(0, 5)
        self.state = self.LEFT_RUN
        if Enemy.image == None:
            Enemy.image = load_image('resource/monster1.png')
        self.dir =1
        self.randNum = random.randint(10,150)
   def update(self):
        self.frame = (self.frame+1) % self.frameSize
        self.x += (self.dir * 2)
        if(self.x > self.startx + self.randNum):
            self.dir = -1
        elif(self.x < self.startx - self.randNum):
            self.dir = 1
   def draw(self):
        self.image.clip_draw(self.frame * 150, self.state * 150, 150, 150, self.x, self.y)
        draw_rectangle(*self.get_bb())
   def get_bb(self):
       return  self.x - 40, self.y - 40, self.x + 40, self.y + 40


class Enemy2:
   image = None
   frameSize = 6
   jump = True
   dir
   LEFT_RUN, RIGHT_RUN,LEFT_HIT,RIGHT_HIT,LEFT_DIE,RIGHT_DIE =7,6,5,4,3,2

   def __init__(self):
        self.x, self.y = random.randint(100, 700), 15
        self.startx = self.x
        self.frame = random.randint(0, 5)
        self.state = self.LEFT_RUN
        if Enemy2.image == None:
            Enemy2.image = load_image('resource/monster2.png')
        self.dir =1
        self.randNum = random.randint(10,150)
   def update(self):


        self.frame = (self.frame+1) % self.frameSize
        self.x += (self.dir * 2)
        if(self.x > self.startx + self.randNum):
            self.dir = -1
            self.frame = 0
        elif(self.x < self.startx - self.randNum):
            self.dir = 1
            self.frame = 0
        if(self.dir == 1 ):
            self.state = self.RIGHT_RUN
        elif(self.dir == -1):
            self.state = self.LEFT_RUN
        #
   def draw(self):
        self.image.clip_draw(self.frame * 300, self.state * 300, 300, 300, self.x, self.y)

class Enemy3:
   image = None
   frameSize = 6
   jump = True
   dir
   LEFT_RUN, RIGHT_RUN,LEFT_HIT,RIGHT_HIT,LEFT_DIE,RIGHT_DIE =7,6,5,4,3,2

   def __init__(self):
        self.x, self.y = random.randint(100, 700), 130
        self.startx = self.x
        self.frame = random.randint(0, 5)
        self.state = self.LEFT_RUN
        self.dir =1
        self.randNum = random.randint(10,150)
   def update(self):

        Enemy3.image = load_image("resource/enemy/move_%d.png"%self.frame)
        self.frame = (self.frame+1) % 11
        self.x += (self.dir * 2)
        if(self.x > self.startx + self.randNum):
            self.dir = -1
            self.frame = 0
        elif(self.x < self.startx - self.randNum):
            self.dir = 1
            self.frame = 0
        if(self.dir == 1 ):
            self.state = self.RIGHT_RUN
        elif(self.dir == -1):
            self.state = self.LEFT_RUN
        #
   def draw(self):
        self.image.draw(self.x, self.y)


class Boss:
   image = None
   frameSize = 6
   jump = True
   dir
   LEFT_IDLE, RIGHT_IDLE, LEFT_RUN, RIGHT_RUN,LEFT_HIT,RIGHT_HIT,LEFT_DIE,RIGHT_DIE =7,6,5,4,3,2,1,0

   def __init__(self):
        self.x, self.y = 400,330
        self.frame = random.randint(0, 5)
        if Boss.image == None:
            Boss.image = load_image('resource/zakum.png')

   def update(self):
        self.frame = (self.frame+1) % self.frameSize

   def draw(self):
        self.image.clip_draw(self.frame * 400, 0, 400, 400, self.x, self.y)


class BossArm1:
   image = None
   def __init__(self):
        self.x, self.y = 400,330
        self.frame = random.randint(0, 5)
        if Boss.image == None:
            Boss.image = load_image('resource/zakum.png')

   def update(self):
        self.frame = (self.frame+1) % self.frameSize

   def draw(self):
        self.image.clip_draw(self.frame * 400, 0, 400, 400, self.x, self.y)
