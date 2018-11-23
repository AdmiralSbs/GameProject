# RohanChandra
# rc8yw

import gamebox
import pygame
import smartbox

xscale = 50
yscale = 50

object = gamebox.from_color(300, 550, 'red', 500, 50)

locations = [
    [0,0,0,0,1],
    [0,0,0,0,1],
    [0,0,0,0,1],
    [0,0,0,0,1],
    [0,0,0,0,1]
]
stuff = {
    0: None,
    1: gamebox.from_color(0, 0, 'red', xscale, yscale),
    2: gamebox.from_color(0,0,'lightblue',xscale,yscale)
}

stuff[1].tags = ['move']
stuff[2].tags = ['platform']


scale = 50
walls = smartbox.create_map_from_list(locations, stuff, xscale, yscale)
max_width = len(locations) * scale
max_height = smartbox.max_size(locations) * scale
camera = gamebox.Camera(max_width, max_height)

def tick(keys):
    camera.clear("green")
    for wall in walls:
        if 'move' in wall.tags:

    # smartbox.draw_object(player, camera
    for wall in walls:
        smartbox.draw_object(wall, camera)
    camera.display()


gamebox.timer_loop(30, tick)
