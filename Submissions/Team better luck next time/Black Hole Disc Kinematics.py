import time
import numpy as np
import pygame as pg
import sys,os
import random
import math

FPS = 30
root = pg.display.set_mode((600,600))
pg.display.set_caption('Black Hole Simulator')


class Main:
    def __init__(self):
        self.clock = pg.time.Clock()

        self.black_hole = Black_hole()

        self.dust_cloud_list = []
        for a in range(100):
            dust_cloud = Dust_cloud()
            self.dust_cloud_list.append(dust_cloud)

        self.main_loop()

    def main_loop(self):
        while(True):
            self.clock.tick(FPS)
            root.fill('#FFFFFF')
            pg.draw.circle(root,'#ffa500',(300,300),170)
            pg.draw.circle(root,'#ffbb10',(300,300),160)
            pg.draw.circle(root,'#efa110',(300,300),150)
            pg.draw.circle(root,'#5e3300',(300,300),140)
            pg.draw.circle(root,'#975210',(300,300),130)
            pg.draw.circle(root,'#e1a030',(300,300),120)
            pg.draw.circle(root,'#f2b022',(300,300),110)
            pg.draw.circle(root,'#692605',(300,300),100)
            pg.draw.circle(root,'#ffa500',(300,300),90)
            pg.draw.circle(root,'#ffbb10',(300,300),80)
            pg.draw.circle(root,'#efa110',(300,300),70)
            pg.draw.circle(root,'#5e3300',(300,300),60)
            pg.draw.circle(root,'#975210',(300,300),50)
            pg.draw.circle(root,'#e1a030',(300,300),40)
            pg.draw.circle(root,'#f2b022',(300,300),30)
            pg.draw.circle(root,'#ffa500',(300,300),20)
            pg.draw.circle(root,(000),(self.black_hole.x,self.black_hole.y),10)

            for cloud in self.dust_cloud_list:
                cloud.x,cloud.y = self.calc_pos(cloud.x,cloud.y)
                pg.draw.circle(root,'#00ff00',(cloud.x,cloud.y),4)
            
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    break

    def calc_pos(self,x,y):
        R = math.sqrt((self.black_hole.x-x)**2+(self.black_hole.y-y)**2)
        new_x = self.black_hole.x + R*math.cos(math.acos(((self.black_hole.x-x)/R))+0.05)
        new_y = self.black_hole.y + R*math.sin(math.asin(((self.black_hole.y-y)/R))+0.05)
        return(new_x,new_y)


class Black_hole:
    def __init__(self):
        self.mass = 1e31
        self.radius = 1e15
        self.x,self.y = 300,300

class Dust_cloud:
    def __init__(self):
        self.mass = 1e10
        self.vel = 1e7
        
        self.x,self.y = random.randint(130,470),random.randint(130,470)
        while self.x in range(280,320) and self.y in range(280,320):
            self.x = random.randint(0,600)

Main()
