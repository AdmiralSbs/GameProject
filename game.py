# Watkins, jmw4dx
import pygame
import gamebox
import smartbox


scale = 50
stuff = {
    0: None,
    1: gamebox.from_color(0, 0, "red", scale, scale),
    2: gamebox.from_color(0, 0, "blue", scale, scale),
}
locations = [
    [2] * 10,
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 2, 0, 2, 0, 1, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 1, 2, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2] * 10,
]

walls = smartbox.create_map_from_list(locations, stuff, scale, scale)
max_width = len(locations) * scale
max_height = smartbox.max_size(locations) * scale
camera = gamebox.Camera(200, 200)
player = gamebox.from_color(100, 100, "yellow", 10, 10)

jump_ready = False
# currently_jumping = False
terminal_jump_velocity = -10
terminal_fall_velocity = 15

def tick(keys):
    global jump_ready

    # key_down =  or pygame.K_SPACE in keys
    if pygame.K_w not in keys:
        jump_ready = False

    if jump_ready and pygame.K_w in keys:
        if (player.speedy <= terminal_jump_velocity):
            jump_ready = False
        player.speedy -= 0.5 # - 0.1 * player.speedy

        # currently_jumping = True
        # print("True")
    else:
        player.speedy = min(terminal_fall_velocity, player.speedy + 1.5)


    if pygame.K_a in keys:
        player.move(-5, 0)
    if pygame.K_d in keys:
        player.move(5, 0)
    # if pygame.K_w in keys:
    #    player.move(0, -5)
    # if pygame.K_s in keys:
    #    player.move(0, 5)

    player.move_speed()

    for wall in walls:
        if wall._color == pygame.Color("blue"):
            if player.touches(wall):
                player.move_to_stop_overlapping(wall)
                if (player.top >= max_height):
                    player.bottom = wall.top
            if player.bottom == wall.top and player.right > wall.left and player.left < wall.right:
                jump_ready = True

    camera.x = min(max(player.x, camera.width / 2), max_width - camera.width / 2)
    camera.y = min(max(player.y, camera.height / 2), max_height - camera.height / 2)

    camera.clear("green")
    for wall in walls:
        smartbox.draw_object(wall, camera)
    smartbox.draw_object(player, camera)
    camera.display()


gamebox.timer_loop(30, tick)
