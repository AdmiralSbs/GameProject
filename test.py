# # RohanChandra
# # rc8yw
#
# import gamebox
# import pygame
# import smartbox
# from smartbox import Dialogue

#
# xscale = 50
# yscale = 50
#
# object = gamebox.from_color(300, 550, 'red', 500, 50)
#
# locations = [
#     [0,0,0,0,1],
#     [0,0,0,0,1],
#     [0,0,0,0,1],
#     [0,0,0,0,1],
#     [0,0,0,0,1]
# ]
# stuff = {
#     0: None,
#     1: gamebox.from_color(0, 0, 'red', xscale, yscale),
#     2: gamebox.from_color(0,0,'lightblue',xscale,yscale)
# }
#
# stuff[1].tags = ['move']
# stuff[2].tags = ['platform']
#
#
# scale = 50
# walls = smartbox.create_map_from_list(locations, stuff, xscale, yscale)
# max_width = len(locations) * scale
# max_height = smartbox.max_size(locations) * scale
# camera = gamebox.Camera(max_width, max_height)
#
# def tick(keys):
#     camera.clear("green")
#     for wall in walls:
#         if 'move' in wall.tags:
#
#     # smartbox.draw_object(player, camera
#     for wall in walls:
#         smartbox.draw_object(wall, camera)
#     camera.display()
#
#
# gamebox.timer_loop(30, tick)


# with open("maps\\map2.csv") as file:

# # while True:
# smartbox.camera = gamebox.Camera(400, 400)
# d = Dialogue(100, 36)
# q = d.how_much(
#     "All these horses in my car got me goin' fast / I just wanna do the dash, put my pedal to the max / SKRT SKRT goin' so fast hope I don't crash / SKRT SKRT one false move it will be my last")
# print(q)
#
# import re
#
# regex = re.compile(r'([0-9]+)(\.[0-9]+)?')
# matches = regex.finditer("1.2 3.5 7.8")
# for match in matches:
#     print(match.group(0), match.group(1), match.group(2))

x = [1, 2, 3]
y = list(x)
print(x == y)
print(x is not y)
x[0] = 97
print(x != y)
print(x is not y)
print(y)
print(3 == 3.0)
print(3 is not 3.0)
