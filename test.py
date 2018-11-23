#RohanChandra
#rc8yw

import gamebox
import pygame
import smartbox

xscale = 50
yscale = 50

camera = gamebox.Camera(600,600)
object = gamebox.from_color(300,550,'red',500,50)

def tick(keys):
    camera.clear('lightblue')
    camera.draw(object)
    camera.display()
gamebox.timer_loop(30,tick)