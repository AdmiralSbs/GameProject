# Watkins, jmw4dx
import pygame
import gamebox
import smartbox

scale = 50
stuff = {
    0: None,
    1: gamebox.from_color(0, 0, "red", scale, scale),
    2: gamebox.from_color(0, 0, "blue", scale, scale),
    3: gamebox.from_color(0, 0, "blue", scale, scale),
    4: gamebox.from_color(0, 0, "blue", scale, scale),
}
tags = [
    [],
    [],
    ["wall"],
    ["wall", "platform"],
    ["wall", "ground"]
]

for i in range(len(tags)):
    if stuff[list(stuff.keys())[i]] != None:
        stuff[list(stuff.keys())[i]].tags = tags[i]

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

walls = smartbox.create_map_from_list(locations, stuff, scale, scale)
max_width = len(locations) * scale
max_height = smartbox.max_size(locations) * scale
camera = gamebox.Camera(max_width, max_height)
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

    player.move_speed()

    for wall in walls:
        if "wall" in wall.tags:
            if player.touches(wall):
                player.move_to_stop_overlapping(wall)

    camera.x = min(max(player.x, camera.width / 2), max_width - camera.width / 2)
    camera.y = min(max(player.y, camera.height / 2), max_height - camera.height / 2)

    camera.clear("green")
    for wall in walls:
        smartbox.draw_object(wall, camera)
    smartbox.draw_object(player, camera)
    camera.display()


gamebox.timer_loop(30, tick)
