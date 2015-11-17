import random
from pico2d import *

__author__ = 'user'

class Effect1:
   image = None
   def __init__(self):
        self.frameSize = 20
        self.frame = 0
   def init(self,x,y,frameNum):
        self.x = x
        self.y = y
        self.frame = frameNum
   def update(self):

        self.frame = (self.frame+1) % self.frameSize
   def get_bb(self):
       return  self.x - 40, self.y - 40, self.x + 70, self.y + 40
   def draw(self,x,y):
        Effect1.image = load_image("resource/fireattack/areaWarning_%d.png"%self.frame)
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())

class Effect2:
   image = None
   def __init__(self):
        self.frameSize = 20
        self.frame = 0
   def init(self,x,y,frameNum):
        self.x = x
        self.y = y
        self.frame = frameNum
   def update(self):

        self.frame = (self.frame+1) % self.frameSize
   def get_bb(self):
       return  self.x +50, 0, self.x + 160, 600
   def draw(self,x,y):
       Effect2.image = load_image("resource/attack2/62_%d.png"%self.frame)
       self.image.draw(self.x+100,self.y+250)
       draw_rectangle(*self.get_bb())

class Effect3:
   image = None
   def __init__(self):
        self.frameSize = 20
        self.frame = 0
   def init(self,x,y,frameNum):
        self.x = x
        self.y = y
        self.frame = frameNum
   def update(self):

        self.frame = (self.frame+1) % self.frameSize
   def get_bb(self):
       return  self.x +50, 0, self.x + 160, 600
   def draw(self,x,y):
        Effect3.image = load_image("resource/attack3/areaWarning_%d.png"%self.frame)
        self.image.draw(self.x+100,self.y+250)
        draw_rectangle(*self.get_bb())
