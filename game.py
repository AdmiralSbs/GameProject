# Watkins, jmw4dx
import pygame
import gamebox
import smartbox

"""
The TAs have rebelled! They are strongly unstatisfied with their mediocre pay and lack of college credit! They DEMAND
reform and so have attempted to...dun dun da..UNIONIZE! You, the fearless capitalist, cannot allow this to happen. But
EGADS, the TAs, under the leadership of the dreaded TA Alexander, have kidnapped Princess Upsorn and trapped her in 
the buggy SIS page! It is your job to complete the PAs, defeat the TAs, and save Princess Upsorn! 



Optional Features:
Animation - characters will have various sprite states
Scrolling level - camera will be zoomed in on map based on distance between players
Collectibles - Power ups can spawn that will affect gameplay
Two Players Simultaneously - As described above


"""
scale = 50
camera = gamebox.Camera(400, 400)
stuff = {
    "0": None,
    "1": gamebox.from_image(0, 0, "images\\shrub.png"),
    "2": gamebox.from_color(0, 0, "blue", scale, scale),
    "3": gamebox.from_color(0, 0, "red", scale, scale),
    "4": gamebox.from_color(0, 0, "blue", scale, scale),
    "5": gamebox.from_image(0, 0, "images\\mountain.png")
}
stuff["1"].width = scale / 2
stuff["5"].width = scale / 2

tags = [
    [],
    ["shrub"],
    ["wall"],
    ["wall", "platform"],
    ["wall", "ground"],
    ["mountain"],
]

for i in range(len(tags)):
    if stuff[list(stuff.keys())[i]] != None:
        stuff[list(stuff.keys())[i]].tags = tags[i]
"""
A sample of what a map could look like (made in program)
locations = [
    [2] * 10,
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [2, 0, 3, 0, 3, 0, 1, 3, 0, 4],
    [2, 0, 3, 0, 3, 0, 1, 3, 0, 4],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [2] * 10,
]
"""

locations2 = smartbox.create_list_from_excel("maps\\map1.csv")

walls = smartbox.create_map_from_list(locations2, stuff, scale, scale)
shrubs = []
for wall in walls:
    if "shrub" in wall.tags:
        shrubs.append(wall)

for shrub in shrubs:
    walls.remove(shrub)

max_width = len(locations2) * scale
max_height = smartbox.max_size(locations2) * scale
# camera = gamebox.Camera(max_width, max_height)
player = gamebox.from_color(100, 100, "yellow", 10, 10)


def tick(keys):
    if pygame.K_a in keys:
        player.move(-5, 0)
    if pygame.K_d in keys:
        player.move(5, 0)
    if pygame.K_w in keys:
        player.move(0, -5)
    if pygame.K_s in keys:
        player.move(0, 5)

    # player.move_speed()

    for wall in walls:
        if "wall" in wall.tags:
            if player.touches(wall):
                player.move_to_stop_overlapping(wall)

    camera.x = min(max(player.x, camera.width / 2), max_width - camera.width / 2)
    camera.y = min(max(player.y, camera.height / 2), max_height - camera.height / 2)

    camera.clear("green")
    for wall in walls:
        smartbox.draw_object(wall, camera)
    for shrub in shrubs:
        smartbox.draw_object(shrub, camera)
    smartbox.draw_object(player, camera)
    camera.display()


gamebox.timer_loop(30, tick)
