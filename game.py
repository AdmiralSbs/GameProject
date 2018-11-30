# Watkins, jmw4dx
import pygame
import gamebox
import smartbox
import items
import dialogue

is_ready = False

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
    "5": gamebox.from_image(0, 0, "images\\mountain.png"),

}
stuff2 = {
    "0": None,
    "1": gamebox.from_color(0, 0, "blue", scale, scale),
    "2": gamebox.from_color(0, 0, "cyan", scale, scale),
    "3": gamebox.from_color(0, 0, "darkblue", scale, scale),
    "4": items.for_loop.object,
    "5": items.while_loop.object,
    "6": items.dictionary.object,
    "7": items.list.object,
    '8': items.enemy1.object,
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
tags2 = [
    [],
    ["wall"],
    [],
    [],
    ["pick_up"],
    ["pick_up"],
    ["pick_up"],
    ["pick_up"],
    ['enemy', 'pick_up'],
]

smartbox.add_tags_to_dict(stuff, tags)
smartbox.add_tags_to_dict(stuff2, tags2)
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

locations2 = smartbox.create_list_from_excel("maps\\map2.csv")

walls = smartbox.create_map_from_list(locations2, stuff2, scale, scale)
shrubs = []
items1 = []
for wall in walls:
    if "shrub" in wall.tags:
        shrubs.append(wall)
    if "pick_up" in wall.tags:
        items1.append(wall)

for shrub in shrubs:
    walls.remove(shrub)
for item in items1:
    walls.remove(item)

max_width = len(locations2) * scale
max_height = smartbox.max_size(locations2) * scale
# camera = gamebox.Camera(max_width, max_height)
player = gamebox.from_color(100, 100, "yellow", 10, 10)


def tick(keys):
    global count
    if pygame.K_a in keys:
        player.move(-5, 0)
    if pygame.K_d in keys:
        player.move(5, 0)
    if pygame.K_w in keys:
        player.move(0, -5)
    if pygame.K_s in keys:
        player.move(0, 5)
    if pygame.K_SPACE in keys:
        is_ready = True
        if is_ready:
            #Write Code Here
    else:
        is_ready = False


    # player.move_speed()

    for wall in walls:
        if "wall" in wall.tags:
            if player.touches(wall):
                player.move_to_stop_overlapping(wall)
    for item in items1:
        if "pick_up" in item.tags and 'enemy' not in item.tags:
            if player.touches(item):
                item.tags.remove("pick_up")
                items.inventory.append(item)
        if 'enemy' in item.tags:
            if player.touches(item):
                player.move_to_stop_overlapping(item)




    camera.x = min(max(player.x, camera.width / 2), max_width - camera.width / 2)
    camera.y = min(max(player.y, camera.height / 2), max_height - camera.height / 2)

    camera.clear("green")
    for wall in walls:
        smartbox.draw_object(wall, camera)
    for shrub in shrubs:
        smartbox.draw_object(shrub, camera)
    for item in items1:
        if "pick_up" in item.tags:
            smartbox.draw_object(item, camera)
    smartbox.draw_object(player, camera)
    camera.display()


gamebox.timer_loop(30, tick)
