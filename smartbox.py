# Watkins, jmw4dx
# Yes, I just did this
import gamebox


def max_size(listy):
    """Given a 2D list, find the length of the largest list within
    :param listy: 2D list
    :return: Length of longest list
    """
    return max([len(x) for x in listy])


def draw_object(sprite, camera):
    """Given a SpriteBox and Camera, determine whether the sprite is on screen (they are overlapping)
    :param sprite:  A SpriteBox object as defined by gamebox
    :param camera:  A Camera object as defined by gamebox
    :return: None
    """
    # Custom errors to make me feel special
    if not isinstance(sprite, gamebox.SpriteBox):
        raise Exception("First parameter must be SpriteBox")
    if not isinstance(camera, gamebox.Camera):
        raise Exception("Second parameter must be Camera")

    checks = [sprite.left < camera.right, sprite.right > camera.left,
              sprite.top < camera.bottom, sprite.bottom > camera.top]
    if True in checks:
        sprite.draw(camera)


# blocks = {0: gamebox.from_color(0, 0, "red", 50, 50)}


def create_map_from_list(locations, dicty, xscale, yscale):
    """Given a 2D list of id values and a dictionary containing a SpriteBox for each id, generate those SpriteBox objects
    :param locations: 2D list of ids, each interior list is for one x value, each item in that list is for one y value
    :param dicty: Matches each id with a SpriteBox to make a copy of
    :param xscale: The difference in space between each item
    :param yscale: The difference in space between each item
    :return: A list containing all of the created SpriteBoxes
    """
    created = []
    for column in range(len(locations)):
        for row in range((len(locations[column]))):
            iden = locations[column][row]
            if iden not in dicty.keys():
                raise Exception("Locations contained key ", str(iden), "not in dict")
            if isinstance(dicty[iden], gamebox.SpriteBox):
                created.append(dicty[iden].copy_at((column + 0.5) * xscale, (row + 0.5) * yscale))
                created[-1].tags = dicty[iden].tags

    return created


def create_list_from_excel(file):
    """Given an excel file that holds the numbers as they will appear
    Reads in the information, transposes as required and returns
    a properly formatted list of lists

    Fle itself has data organized as it will appear on screen, this method transposes
    that data into the style handled by the above function

    :param file: File location
    :return: List of lists for use in above method
    """
    # Get all the lines
    with open(file) as excel:
        parts = excel.read().split("\n")
    lines = []
    for i in range(len(parts)):
        thing = parts[i].strip("ï»¿")
        lines.append(thing.split(","))

    # Transpose all the lines
    final_lines = []
    for x in range(len(lines[0])):
        final_lines.append([])

    for line in lines:
        if line == [""]: continue
        for spot in range(len(line)):
            if (line[spot] != ""):
                final_lines[spot].append(line[spot])
            else:
                final_lines[spot].append("0")

    # print(lines)
    # print(final_lines)
    return final_lines
