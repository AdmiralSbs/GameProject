# Watkins, jmw4dx
import pygame
import gamebox
import smartbox
import math

win = False

TA_info = """
The TAs have rebelled! They are strongly unstatisfied with their mediocre pay and lack of college credit! They DEMAND
reform and so have attempted to...dun dun da..UNIONIZE! You, the fearless capitalist, cannot allow this to happen. But
OH NO, the TAs, under the leadership of the dreaded TA Alexander, have kidnapped Professor Upsorn and trapped her in 
the Archimedes Server, trapped under her own assignments! It is your job to help her complete the PAs and defeat TAs!

It's basically Pokemon/Undertale.

Players will move around a 2d map, collect items, and engage in pokemon style combat with enemies. They will have to 
defeat a final boss.

The maps are not too large, and link to each other

The PA's are some of our "favorites" that will basically be like strength boulders, rock smash rocks, etc., with
specific skills relating to the class serving like HMs that allow you to further progress in the game.

Optional Features:
Health Bar - Will be present during battle. A loss requires restarting the game (you learn from loss anyhow)
Scrolling level - camera will be zoomed in on map based on distance between players
Collectibles - Power ups can spawn that will affect gameplay
Enemies - They're there, they move, they are both easily handled and can easily handle you
File Reading - Every map comes from a file
"""


camera = smartbox.camera
inventory = []
kills = 0

maps = [
    smartbox.read_map_objects("map0.csv"),
    smartbox.read_map_objects("map1.csv"),
    smartbox.read_map_objects("map2.csv"),
    smartbox.read_map_objects("map3.csv"),
    smartbox.read_map_objects("map4.csv"),
    smartbox.read_map_objects("map5.csv"),
]
curr_map = 0


def the_map():
    return maps[curr_map]


def calc_maxes():
    global max_width, max_height
    max_width = len(the_map().locations) * the_map().scale
    max_height = smartbox.max_size(the_map().locations) * the_map().scale


just_warped = False


def warp_player(new_map, xloc, yloc):
    global curr_map
    curr_map = new_map
    player.x = (xloc + 0.5) * the_map().scale
    player.y = (yloc + 0.5) * the_map().scale
    calc_maxes()


player = smartbox.Handler.upsorn

warp_player(0, 3, 1)

big_dialogue: smartbox.Dialogue = smartbox.Dialogue(400, 36)
d_battle: smartbox.Dialogue = smartbox.Dialogue(200, 36)

disp_pause = False
box = "list_pu"
enemy = None
info = []
info.append("{Press Space} Dear TA: Please read game.py for what you need in terms of grading")
info.append("""The TAs have rebelled! They DEMAND wage reform and have attempted to UNIONIZE! The TAs, under the 
leadership of the dreaded TA Alexander, have kidnapped Professor Upsorn and trapped her in the Archimedes Server,
under the weight of her own assignments! It is your job to help her complete the PAs and defeat the TAs! {Press Space}""")
info.append("""Welcome to ESCAPE FROM ARCHIMEDES!!! Play as Upsorn (the yellow square) to escape the Archimedes
server. Use W-A-S-D to move around and SPACE to advance through text.  Python skills are lying on the ground to pick up,
just walk to them. Use them to complete PA's and advance.""")
info.append("""Moving squares are unionizing TA's, touch them to start a battle. You will have four attacks at your disposal.
Press 1-2-3-4 to select your attack for the turn. They all do the same damage, but are weaker the second time.
Your health resets after each battle. Pick up skills and defeat weaker TA's to get stronger. 
You'll need everything you have to defeat the great TA Alexander.""")

the_big_sheet = big_dialogue.text_sprites_list(info)
box3 = 0


def start_screen(keys):
    global box3
    if pygame.K_SPACE in keys:
        box3 += 1
        if box3 == len(the_big_sheet):
            gamebox.stop_loop()
            return
        keys.clear()
    camera.clear("white")
    smartbox.draw_object(big_dialogue.background)
    for t in the_big_sheet[box3]:
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
    global disp_pause, box, enemy, just_warped, the_gate
    gen_move(keys)
    if pygame.K_SPACE in keys:
        keys.remove(pygame.K_SPACE)
        if "_pu" in box or "_no" in box:
            disp_pause = False
        elif "meet" in box:
            battle_prep()
            disp_pause = False
            if player.health <= 0 or win:
                gamebox.stop_loop()
                return
        elif "_yes" in box:
            disp_pause = False
            the_map().remove(the_gate)

    for wall in the_map().get_list("wall"):
        if player.touches(wall):
            player.move_to_stop_overlapping(wall)

    for item in the_map().get_list("pick_up"):
        if player.touches(item):
            the_map().remove(item)
            inventory.append(item.name.lower())
            disp_pause = True
            box = item.name.lower() + "_pu"

    for item in the_map().get_list("enemy"):
        if item.health == 0:
            continue
        if player.touches(item):
            player.move_to_stop_overlapping(item)
            enemy = item
            box = enemy.name.lower() + "_meet"
            disp_pause = True
        if "vertical" in item.tags and not disp_pause:
            if item.speedy == 0:
                item.speedy = 1
            for wall in the_map().get_list("wall"):
                if wall.touches(item):
                    item.speedy *= -1
            item.move_speed()
        if "horizontal" in item.tags and not disp_pause:
            if item.speedx == 0:
                item.speedx = 1
            for wall in the_map().get_list("wall"):
                if wall.touches(item):
                    item.speedx *= -1
            item.move_speed()

    for gate in the_map().get_list("gate"):
        if player.touches(gate):
            item = smartbox.Handler.all_items[gate.tags[2]].name.lower()
            if item in inventory:
                box = "gate_" + item + "_yes"
                the_gate = gate
            else:
                box = "gate_" + item + "_no"
            disp_pause = True
            player.move_to_stop_overlapping(gate)
            if player.left_touches(gate):
                player.x += 5
            if player.top_touches(gate):
                player.y += 5
            if player.right_touches(gate):
                player.x -= 5
            if player.bottom_touches(gate):
                player.y -= 5

    check = False
    for warp in the_map().get_list("warp"):
        if player.touches(warp):
            check = True
            parts = the_map().warps[warp.tags[1]]
            if not just_warped:
                warp_player(parts[0], parts[1], parts[2])
    just_warped = check

    camera.x = min(max(player.x, camera.width / 2), max_width - camera.width / 2)
    camera.y = min(max(player.y, camera.height / 2), max_height - camera.height / 2)

    camera.clear("green")
    for tile in the_map().get_list("tile"):
        smartbox.draw_object(tile)
    for item in the_map().get_list("top"):
        smartbox.draw_object(item)
    smartbox.draw_object(player)

    the_map().dialogue.update_loc(True)
    if disp_pause:
        smartbox.draw_object(the_map().dialogue.background)
        for thing in the_map().cool_boxes[box]:
            smartbox.draw_object(thing)

    camera.display()


cool_lines2 = None

choices = [0, 0, 0, 0]


def battle_prep():
    global cool_lines2, choices, pl, en, box2
    player.level = len(inventory)
    player.max_health = player.level * 20
    player.health = player.max_health

    choices = [0, 0, 0, 0]
    box2 = 0
    d_battle.update_loc(True)
    cool_lines2_text = [
        player.name + " is challenged by TA " + enemy.title + " " + enemy.name + "!",
        "1: " + player.move_list[0][0] + " 2: " + player.move_list[1][0] + " 3: " + player.move_list[2][0] + " 4: " +
        player.move_list[3][0],
        player.name + " used " + player.move_list[0][0] + " , " + player.move_list[0][1],
        player.name + " used " + player.move_list[1][0] + " , " + player.move_list[1][1],
        player.name + " used " + player.move_list[2][0] + " , " + player.move_list[2][1],
        player.name + " used " + player.move_list[3][0] + " , " + player.move_list[3][1],
        enemy.name + " used " + enemy.move_list[0][0] + " , " + enemy.move_list[0][1],
        enemy.name + " used " + enemy.move_list[1][0] + " , " + enemy.move_list[1][1],
        enemy.name + " used " + enemy.move_list[2][0] + " , " + enemy.move_list[2][1],
        enemy.name + " used " + enemy.move_list[3][0] + " , " + enemy.move_list[3][1],
        enemy.name + " fainted!",
        player.name + " fainted!"
    ]
    cool_lines2 = d_battle.text_sprites_list(cool_lines2_text)
    pl = gamebox.from_image(0, 0, 'images\\Upsorn.png')
    en = enemy.copy()
    pl.scale_by(100 / pl.height)
    en.scale_by(100 / en.height)
    pl.x = 100 + camera.left
    pl.y = 100 + camera.top
    en.x = 300 + camera.left
    en.y = 100 + camera.top

    gamebox.timer_loop(30, battle)

    gamebox._timeron = True
    gamebox.unpause()

    if (enemy.health <= 0):
        if enemy.level == 11:
            global win
            win = True
        the_map().remove(enemy)
        player.health = player.max_health
        global kills
        kills += 1


def battle(keys):
    global box2, choices

    if box2 == 1:
        attacked = True
        if pygame.K_1 in keys:
            box2 = 2
        elif pygame.K_2 in keys:
            box2 = 3
        elif pygame.K_3 in keys:
            box2 = 4
        elif pygame.K_4 in keys:
            box2 = 5
        else:
            attacked = False
        if attacked:
            damage = math.ceil(player.level * 5 * (0.5 ** choices[box2 - 2])) + kills
            enemy.health = max(enemy.health - damage, 0)
            choices[box2 - 2] += 1
        keys.clear()

    if pygame.K_SPACE in keys:
        keys.clear()
        if box2 in [0, 6, 7, 8, 9]:
            if player.health > 0:
                box2 = 1
            else:
                box2 = 11
        elif box2 in [2, 3, 4, 5]:
            if enemy.health > 0:
                box2 += 4
                damage = enemy.level * 4
                player.health = max(player.health - damage, 0)
            else:
                box2 = 10
        elif box2 == 10 or box2 == 11:
            gamebox.stop_loop()
    camera.clear("black")

    smartbox.draw_object(d_battle.background)
    for thing in cool_lines2[box2]:
        smartbox.draw_object(thing)
    smartbox.draw_object(pl)
    smartbox.draw_object(en)
    w1 = min((player.max_health - player.health) / player.max_health * 100, 100)
    w2 = min((enemy.max_health - enemy.health) / enemy.max_health * 100, 100)
    g1 = gamebox.from_color(100 + camera.left, 25 + camera.top, "green", 100, 30)
    g2 = gamebox.from_color(300 + camera.left, 25 + camera.top, "green", 100, 30)
    h1 = gamebox.from_color(0, 25 + camera.top, "red", w1, 30)
    h1.right = g1.right
    h2 = gamebox.from_color(0, 25 + camera.top, "red", w2, 30)
    h2.right = g2.right

    t1 = str(player.title) + " " + str(player.name) + " (" + str(player.level) + ")"
    t11 = gamebox.from_text(0, 175 + camera.top, t1, 24, "gold")
    t11.left = g1.left
    t2 = str(enemy.title) + " " + str(enemy.name) + " (" + str(enemy.level) + ")"
    t22 = gamebox.from_text(0, 175 + camera.top, t2, 24, "gold")
    t22.right = g2.right

    smartbox.draw_object(t11)
    smartbox.draw_object(t22)
    smartbox.draw_object(g1)
    smartbox.draw_object(g2)
    smartbox.draw_object(h1)
    smartbox.draw_object(h2)
    smartbox.draw_object(gamebox.from_text(g1.x, g1.y, str(player.health) + "/" + str(player.max_health), 40, "gold"))
    smartbox.draw_object(gamebox.from_text(g2.x, g2.y, str(enemy.health) + "/" + str(enemy.max_health), 40, "gold"))

    camera.display()


playing = True
gamebox.timer_loop(30, start_screen)
gamebox.timer_loop(30, tick)
if player.health <= 0:
    info_end = "Well, you lost, big OOF"
elif win:
    info_end = """Yo-yo-you did it?!?  You defeated the Great TA Alexander?  Unbelievable!  Tbh this was in honor of all
    we've learned this year in CS, because we really did get better (hence this game).  If you legit beat the game, you
    had to defeat every enemy, so props to you!  Thanks so much for playing!"""
else:
    info_end = "Quitter, you didn't bother to try..."
the_big_sheet = big_dialogue.create_text_sprites(big_dialogue.calc_lines(info_end))
big_dialogue.update_loc(True)


def end_screen(keys):
    if pygame.K_SPACE in keys:
        gamebox.stop_loop()
    camera.clear("white")
    smartbox.draw_object(big_dialogue.background)
    for t in the_big_sheet:
        smartbox.draw_object(t)
    camera.display()


gamebox.timer_loop(30, end_screen)
