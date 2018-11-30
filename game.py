# Watkins, jmw4dx
import pygame
import gamebox
import smartbox
import items
from dialogue import Dialogue

is_ready = False

info = """
The TAs have rebelled! They are strongly unstatisfied with their mediocre pay and lack of college credit! They DEMAND
reform and so have attempted to...dun dun da..UNIONIZE! You, the fearless capitalist, cannot allow this to happen. But
EGADS, the TAs, under the leadership of the dreaded TA Alexander, have kidnapped Professor Upsorn and trapped her in 
the Archimedes Server! It is your job to complete the PAs and defeat TAs! (notice the rhyme?)

It's basically Pokemon.

Players will move around a 2d map, collect items, and engage in pokemon style combat with enemies. They will have to 
defeat a final boss.

The maps are not too large, and link to each other

The PA's are some of our "favorites" that will basically be like strength boulders, rock smash rocks, etc., with specific
skills relating to the class serving like HMs that allow you to further progress in the game.



Optional Features:
Health Bar - Will be present during battle. A loss requires reloading a previous save (DOOM style) (nyi)
Scrolling level - camera will be zoomed in on map based on distance between players (implemented)
Collectibles - Power ups can spawn that will affect gameplay (implemented)
Intersession Progress - Game will autosave on quit, and allow for manual saves as well (nyi)

"""
scale = 50
camera = gamebox.Camera(400, 400)

stuff2 = {
    "0": None,
    "1": gamebox.from_color(0, 0, "blue", scale, scale),
    "2": gamebox.from_color(0, 0, "cyan", scale, scale),
    "3": gamebox.from_color(0, 0, "darkblue", scale, scale),
    "4": items.for_loop,
    "5": items.while_loop,
    "6": items.dictionary,
    "7": items.list,
    '8': items.enemy1,
    '9': items.upsorn,
}

tags2 = [
    [],
    ["wall"],
    [],
    [],
    ["pick_up", 'top'],
    ["pick_up", 'top'],
    ["pick_up", 'top'],
    ["pick_up", 'top'],
    ['enemy', 'top'],
    ['player', 'top']
]

smartbox.add_tags_to_dict(stuff2, tags2)

locations2 = smartbox.create_list_from_excel("maps\\map2.csv")

walls = smartbox.create_map_from_list(locations2, stuff2, scale, scale)
items1 = []

player = None

for wall in walls:
    if "top" in wall.tags:
        print("hey")
        items1.append(wall)
    if "player" in wall.tags:
        print("found")
        player = wall

for item in items1:
    walls.remove(item)

max_width = len(locations2) * scale
max_height = smartbox.max_size(locations2) * scale

if player == None:
    player = gamebox.from_color(100, 100, "green", 10, 10)

d = Dialogue()
d.setup(100, 36, camera)
cool_lines = [
    d.calc_lines("You picked up the LIST ability damn right you did boy"),
    d.calc_lines("You picked up the DICT ability"),
    d.calc_lines("I can't believe it!  You're still moving...  Prepare to perish!"),
]
cool_boxes = [
    d.create_text_sprites(cool_lines[0]),
    d.create_text_sprites(cool_lines[1]),
    d.create_text_sprites(cool_lines[2]),
]

disp_pause = False
timer_end = 0
timer = 0
box = 0
enemy = None

info2 = """Peep game.py and the readme.txt for some cool stuff. Use WASD to move around, and touch the red guy to start
a fight.  Oooh, spooky.  WELCOME TO ESCAPE FROM ARCHIMEDES: ATTACK OF THE TA's AND THE PA's.  Oooh, aaah.  SPACE to
get out of these text situations, 1-4 when appropriate. X-ing out the window enough times closes it.  Please hit up the
readme.txt
"""
d.setup(400, 36, camera)
the_big_sheet = d.create_text_sprites(d.calc_lines(info2))


def start_screen(keys):
    if pygame.K_SPACE in keys:
        gamebox.stop_loop()
    camera.clear("white")
    smartbox.draw_object(d.background, camera)
    for t in the_big_sheet:
        smartbox.draw_object(t, camera)
    camera.display()


def tick(keys):
    global timer, timer_end, disp_pause, box, enemy
    timer += 0

    if not disp_pause:
        if pygame.K_a in keys:
            player.move(-5, 0)
        if pygame.K_d in keys:
            player.move(5, 0)
        if pygame.K_w in keys:
            player.move(0, -5)
        if pygame.K_s in keys:
            player.move(0, 5)
    if pygame.K_SPACE in keys:
        if box == 1 or box == 0:
            disp_pause = False
        elif box == 2:
            disp_pause = False
            battle_prep(player, enemy)
            items1.remove(enemy)
            disp_pause = False

    for wall in walls:
        if "wall" in wall.tags:
            if player.touches(wall):
                player.move_to_stop_overlapping(wall)
    for item in items1:
        if "pick_up" in item.tags and 'enemy' not in item.tags:
            if player.touches(item):
                item.tags.remove("pick_up")
                items.inventory.append(item)
                disp_pause = True
                vals = {
                    "LIST": 0,
                    "DICT": 1,
                }
                # item.hi()
                # print(item.__dict__.keys())
                box = vals[item.name]

        if 'enemy' in item.tags:
            if player.touches(item):
                player.move_to_stop_overlapping(item)
                box = 2
                disp_pause = True
                enemy = item

    camera.x = min(max(player.x, camera.width / 2), max_width - camera.width / 2)
    camera.y = min(max(player.y, camera.height / 2), max_height - camera.height / 2)

    a, b = d.update_loc(camera, cool_boxes)
    for group in cool_boxes:
        for thing in group:
            thing.x += a
            thing.y += b

    camera.clear("green")
    for wall in walls:
        smartbox.draw_object(wall, camera)
    for item in items1:
        if "pick_up" or "enemy" in item.tags:
            smartbox.draw_object(item, camera)

    smartbox.draw_object(player, camera)

    if disp_pause:
        smartbox.draw_object(d.background, camera)
        for thing in cool_boxes[box]:
            smartbox.draw_object(thing, camera)

    camera.display()


# enemy_moves = ['Vague Answer', 'We\'re people too' , 'PA Reject', 'Make lab harder at 3:12']

# stages = ["declare", "pick_move", "state_moves", "end"]

cool_lines2 = None


def battle_prep(player, enemy):
    d.setup(100, 36, camera)
    global cool_lines2
    cool_lines2 = [
        d.calc_lines("Upsorn is challenged by TA grunt!"),
        d.calc_lines("1: " + player.move_list[0] + " 2: " + player.move_list[1] +
                     " 3: " + player.move_list[2] + " 4: " + player.move_list[3] + " (try all 4 to \"win\")"),
        d.calc_lines("Upsorn used " + player.move_list[0] + " , a student answered!"),
        d.calc_lines("Upsorn used " + player.move_list[1] + " , she figured out the concept!"),
        d.calc_lines("Upsorn used " + player.move_list[2] + " , it's surprisingly effective..."),
        d.calc_lines("Upsorn used " + player.move_list[3] + " , TA remembers why they chose Upsorn"),
        d.calc_lines("Enemy used " + enemy.move_list[0] + " , but Upsorn won't understand until she's wiser"),
        d.calc_lines(
            "Enemy used " + enemy.move_list[1] + " , Upsorn exhibits increased sympathy (which is hard for her)"),
        d.calc_lines("Enemy used " + enemy.move_list[2] + " , Upsorn doesn't know why"),
        d.calc_lines("Enemy used " + enemy.move_list[3] + " , Upsorn missed the bus!"),
        d.calc_lines("Enemy couldn't handle the lack of mechanics in this part and faints!")
    ]
    # player.scale_by(10)
    # enemy.scale_by(10)
    # coords = [[player.x, player.y], [enemy.x, enemy.y]]
    # player.x = 100
    # player.y = 100
    # enemy.x = 300
    # enemy.y = 100
    gamebox.timer_loop(30, battle)
    # player.scale_by(0.1)
    # enemy.scale_by(0.1)
    # player.x = coords[0][0]
    # player.y = coords[0][1]
    # enemy.x = coords[1][0]
    # enemy.y = coords[1][1]


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
        if (box2 - 1 not in choices):
            choices.append(box2 - 1)
        keys.clear()

    if pygame.K_SPACE in keys:
        keys.clear()
        if box2 in [0, 6, 7, 8, 9]:
            if sum(choices):
                box2 = 10
            else:
                box2 = 1
        elif box2 in [2, 3, 4, 5]:
            box2 += 4
        elif box2 == 10:
            gamebox.stop_loop()
    camera.clear("black")
    camera.draw(gamebox.from_text(50, 50, "hi", 36, "yellow"))
    smartbox.draw_object(gamebox.from_color(100, 100, "yellow", 100, 100), camera)
    smartbox.draw_object(gamebox.from_color(300, 100, "red", 100, 100), camera)
    smartbox.draw_object(d.background, camera)
    for thing in d.create_text_sprites(cool_lines2[box2]):
        smartbox.draw_object(thing, camera)
    camera.display()


d.setup(400, 36, camera)
gamebox.timer_loop(30, start_screen)
d.setup(100, 36, camera)
gamebox.timer_loop(30, tick)
