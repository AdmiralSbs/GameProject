# Watkins, jmw4dx
import pygame
import gamebox
import smartbox

is_ready = False

info = """
The TAs have rebelled! They are strongly unstatisfied with their mediocre pay and lack of college credit! They DEMAND
reform and so have attempted to...dun dun da..UNIONIZE! You, the fearless capitalist, cannot allow this to happen. But
OH NO, the TAs, under the leadership of the dreaded TA Alexander, have kidnapped Professor Upsorn and trapped her in 
the Archimedes Server, trapped under her own assignments! It is your job to help her complete the PAs and defeat TAs!

It's basically Pokemon.

Players will move around a 2d map, collect items, and engage in pokemon style combat with enemies. They will have to 
defeat a final boss.

The maps are not too large, and link to each other

The PA's are some of our "favorites" that will basically be like strength boulders, rock smash rocks, etc., with
specific skills relating to the class serving like HMs that allow you to further progress in the game.

Optional Features:
Health Bar - Will be present during battle. A loss requires reloading a previous save (DOOM style) (nyi)
Scrolling level - camera will be zoomed in on map based on distance between players (implemented)
Collectibles - Power ups can spawn that will affect gameplay (implemented)
Intersession Progress - Game will autosave on quit, and allow for manual saves as well (nyi)
"""

camera = gamebox.Camera(400, 400)
smartbox.camera = camera

inventory = []

map2: smartbox.Map = smartbox.read_map_objects("map2.csv")

player = None

for thing in map2.get_list("player"):
    player = thing

max_width = len(map2.locations) * map2.scale
max_height = smartbox.max_size(map2.locations) * map2.scale

if player is None:
    player = gamebox.from_color(100, 100, "green", 10, 10)

d: smartbox.Dialogue = map2.dialogue
big_dialogue = smartbox.Dialogue(400, 36)
d_battle = smartbox.Dialogue(200, 36)
cool_boxes = d.text_sprites_list(map2.text)

disp_pause = False
timer_end = 0
timer = 0
box = "list_pu"
enemy = None
info2 = """Peep game.py and the readme.txt for some cool stuff. Use WASD to move around, and touch the red guy to start
a fight.  Oooh, spooky.  WELCOME TO ESCAPE FROM ARCHIMEDES: ATTACK OF THE TA's AND THE PA's.  Oooh, aaah.  SPACE to
get out of these text situations, 1-4 when appropriate. X-ing out the window enough times closes it.  Please hit up the
readme.txt
"""
the_big_sheet = big_dialogue.create_text_sprites(big_dialogue.calc_lines(info2))


def start_screen(keys):
    if pygame.K_SPACE in keys:
        gamebox.stop_loop()
    camera.clear("white")
    smartbox.draw_object(big_dialogue.background)
    for t in the_big_sheet:
        smartbox.draw_object(t)
    camera.display()


def gen_move(keys):
    if not disp_pause:
        if pygame.K_a in keys:
            player.move(-5, 0)
        if pygame.K_d in keys:
            player.move(5, 0)
        if pygame.K_w in keys:
            player.move(0, -5)
        if pygame.K_s in keys:
            player.move(0, 5)


def tick(keys):
    global timer, timer_end, disp_pause, box, enemy
    timer += 1
    gen_move(keys)
    if pygame.K_SPACE in keys:
        keys.remove(pygame.K_SPACE)
        if box == "list_pu" or box == "dict_pu":
            disp_pause = False
        elif box == "enemy1":
            disp_pause = False
            battle_prep(player, enemy)
            disp_pause = False

    for wall in map2.objects:
        if "wall" in wall.tags:
            if player.touches(wall):
                player.move_to_stop_overlapping(wall)
    for item in map2.get_list("top"):
        if "pick_up" in item.tags:
            if player.touches(item):
                map2.remove(item)
                inventory.append(item)
                disp_pause = True
                box = item.name.lower() + "_pu"

        if 'enemy' in item.tags:
            if player.touches(item):
                player.move_to_stop_overlapping(item)
                box = "enemy1"
                disp_pause = True
                enemy = item

    camera.x = min(max(player.x, camera.width / 2), max_width - camera.width / 2)
    camera.y = min(max(player.y, camera.height / 2), max_height - camera.height / 2)

    camera.clear("green")
    for tile in map2.get_list("tile"):
        smartbox.draw_object(tile)
    for item in map2.get_list("top"):
        smartbox.draw_object(item)
    smartbox.draw_object(player)

    if disp_pause:
        smartbox.draw_object(d.background)
        for thing in cool_boxes[box]:
            smartbox.draw_object(thing)

    camera.display()


cool_lines2 = None


def battle_prep(player, enemy):
    global cool_lines2
    d_battle.update_loc()
    cool_lines2_text = [
        "Upsorn is challenged by TA grunt!",
        "1: " + player.move_list[0] + " 2: " + player.move_list[1] + "3: " + player.move_list[2] + " 4: " +
        player.move_list[3] + " (try all 4 to \"win\")",
        "Upsorn used " + player.move_list[0] + " , a student answered!",
        "Upsorn used " + player.move_list[1] + " , she figured out the concept!",
        "Upsorn used " + player.move_list[2] + " , it's surprisingly effective...",
        "Upsorn used " + player.move_list[3] + " , TA remembers why they chose Upsorn",
        "Enemy used " + enemy.move_list[0] + " , but Upsorn won't understand until she's wiser",
        "Enemy used " + enemy.move_list[1] + " , but Upsorn's sympathy was already at max",
        "Enemy used " + enemy.move_list[2] + " , Upsorn doesn't know what's wrong with her code",
        "Enemy used " + enemy.move_list[3] + " , Upsorn missed the bus trying to finish!",
        "Enemy couldn't handle the lack of mechanics in this part and faints!",
    ]
    cool_lines2 = d_battle.text_sprites_list(cool_lines2_text)
    player.scale_by(10)
    enemy.scale_by(10)
    coords = [[player.x, player.y], [enemy.x, enemy.y]]
    player.x = 100 + camera.left
    player.y = 100 + camera.top
    enemy.x = 300 + camera.left
    enemy.y = 100 + camera.top
    gamebox.timer_loop(30, battle)
    player.scale_by(0.1)
    enemy.scale_by(0.1)
    player.x = coords[0][0]
    player.y = coords[0][1]
    enemy.x = coords[1][0]
    enemy.y = coords[1][1]
    gamebox._timeron = True
    gamebox.unpause()
    map2.remove(enemy)


stage = "declare"
box2 = 0
choices = []


def battle(keys):
    global stage, box2, choices

    if box2 == 1:
        if pygame.K_1 in keys:
            box2 = 2
        elif pygame.K_2 in keys:
            box2 = 3
        elif pygame.K_3 in keys:
            box2 = 4
        elif pygame.K_4 in keys:
            box2 = 5
        if box2 - 1 not in choices:
            choices.append(box2 - 1)
        keys.clear()

    if pygame.K_SPACE in keys:
        keys.clear()
        if box2 in [0, 6, 7, 8, 9]:
            if sum(choices) == 10:
                box2 = 10
            else:
                box2 = 1
        elif box2 in [2, 3, 4, 5]:
            box2 += 4
        elif box2 == 10:
            gamebox.stop_loop()
    camera.clear("black")

    smartbox.draw_object(d_battle.background)
    for thing in cool_lines2[box2]:
        smartbox.draw_object(thing)
    smartbox.draw_object(player)
    smartbox.draw_object(enemy)
    camera.display()


gamebox.timer_loop(30, start_screen)
gamebox.timer_loop(30, tick)
