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
        Effect1.image = load_image("resource/fireattack/areaWarning_%d.png"%self.frame)
        self.frame = (self.frame+1) % self.frameSize
   def get_bb(self):
       return  self.x - 40, self.y - 40, self.x + 70, self.y + 40
   def draw(self):
        self.image.draw(self.x,self.y )
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
        Effect1.image = load_image("resource/fireattack/areaWarning_%d.png"%self.frame)
        self.frame = (self.frame+1) % self.frameSize
   def get_bb(self):
       return  self.x - 40, self.y - 40, self.x + 70, self.y + 40
   def draw(self):
        self.image.draw(self.x,self.y )
        draw_rectangle(*self.get_bb())
