# Watkins, jmw4dx
# Yes, I just did this
import gamebox
from pathlib import Path
import re

camera: gamebox.Camera = None


def max_size(listy):
    """Given a 2D list, find the length of the largest list within
    :param listy: 2D list
    :return: Length of longest list
    """
    return max([len(x) for x in listy])


def transpose(listy):
    """Given a 2D list, transpose it
    As written on https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
    :param listy: 2D list
    :return: transposed list
    """
    return [[listy[j][i] for j in range(len(listy))] for i in range(len(listy[0]))]


def move_extras(copy, og):
    big_keys = list(og.__dict__.keys())
    reg = ['x', 'y', 'speedx', 'speedy', '_key', '_image', '_color', '_w', '_h']
    for r in reg:
        big_keys.remove(r)
    for b in big_keys:
        copy.__dict__[b] = og.__dict__[b]


def draw_object(sprite):
    """Given a SpriteBox (and assuming camera was set) determine whether the sprite is on screen (they are overlapping)
    :param sprite:  A SpriteBox object as defined by gamebox
    :return: None
    """
    # Custom errors to make me feel special
    if not isinstance(sprite, gamebox.SpriteBox):
        raise Exception("First parameter must be SpriteBox")
    if not isinstance(camera, gamebox.Camera):
        raise Exception("Smartbox camera must be set")

    checks = [sprite.left < camera.right, sprite.right > camera.left,
              sprite.top < camera.bottom, sprite.bottom > camera.top]
    if True in checks:
        sprite.draw(camera)


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
            for i in iden.split("|"):
                if i not in dicty.keys():
                    raise Exception("Locations contained key ", str(i), "not in dict")
                if isinstance(dicty[i], gamebox.SpriteBox):
                    created.append(dicty[i].copy_at((column + 0.5) * xscale, (row + 0.5) * yscale))
                    created[-1].tags = dicty[i].tags
                    move_extras(created[-1], dicty[i])

    return created


def make_item(self, name, style, weight):
    self.name = name
    self.style = style
    self.weight = weight


def make_entity(self, name, move_list, level):
    self.name = name
    self.move_list = move_list
    self.max_health = level * 20
    self.level = level
    self.health = self.max_health


def add_tags_to_dict(stuff, tags):
    for key in tags.keys():
        if stuff[key] is not None:  # if stuff[key] != None
            stuff[key].tags = tags[key]


def sort_objects(map):
    """Given a map, sort its objects into a dictionary by its categories

    :param objects: List of spriteboxes
    :param categories: List of strings
    :return: None
    """
    categories = map.categories
    objects = map.objects

    for cat in categories:
        map.__dict__[cat + "_list"] = []
    for thing in objects:
        if thing is not None:
            if "tags" in thing.__dict__:
                for tag in thing.tags:
                    if tag in categories:
                        map.__dict__[tag + "_list"].append(thing)


class Handler:
    # Watkins, jmw4dx
    import gamebox

    styles = ["key"]
    names = ['Sean', 'Alexander']
    upsorn_moves = ['Ask Question on Piazza', 'Watch Live Code', 'Attend Lecture', 'Wholesome Email']
    enemy_moves = ['Vague Answer', 'You know we\'re people too', 'PA Rejected', 'Make lab harder at 3:12pm']

    for_loop = gamebox.from_text(0, 0, "FOR", 12, "yellow", bold=True, italic=False)
    make_item(for_loop, "for_loop", 'key', '1')
    while_loop = gamebox.from_text(0, 0, "WHILE", 12, "red", bold=True, italic=False)
    make_item(while_loop, 'while_loop', 'key', '2')
    dictionary = gamebox.from_text(0, 0, "DICT", 12, "lightblue", bold=True, italic=False)
    make_item(dictionary, 'dict', 'key', '3')
    list_ = gamebox.from_text(0, 0, "LIST", 12, "gray", bold=True, italic=False)
    make_item(list_, "list", 'key', '4')
    print_ = gamebox.from_text(0, 0, "PRINT", 12, "gray", bold=True, italic=False)
    make_item(print_, "print", 'key', '0')
    if_ = gamebox.from_text(0, 0, "IF", 12, "gray", bold=True, italic=False)
    make_item(if_, "if", 'key', '6')
    elseif_ = gamebox.from_text(0, 0, "ELSE_IF", 12, "gray", bold=True, italic=False)
    make_item(elseif_, "elseif", 'key', '7')

    enemy1 = gamebox.from_color(0, 0, 'red', 10, 10)
    make_entity(enemy1, 'Bob', enemy_moves, 50)
    enemy2 = gamebox.from_color(0, 0, 'purple', 10, 10)
    make_entity(enemy2, 'Joe', enemy_moves, 50)
    upsorn = gamebox.from_color(0, 0, 'yellow', 10, 10)
    make_entity(upsorn, 'Upsorn', upsorn_moves, 50)

    all_items = {
        "for_loop": for_loop,
        "while_loop": while_loop,
        "dict": dictionary,
        "list": list_,
        "print": print_,
        "if": if_,
        "elseif": elseif_,
    }

    all_entities = {
        "enemy1": enemy1,
        "upsorn": upsorn,
        "enemy2": enemy2,
    }


class Dialogue:
    """This class handles the display of text in a "dialogue box" format similar to pokemon
    Given a string and a text size, it sorts it into rows that will fit on the screen
    """
    buffer = 5

    def __init__(self, h: int, fs: int):
        self.background = gamebox.from_color(0, 0, "white", camera.width, h)
        self.background.left = camera.left
        self.background.bottom = camera.bottom
        self.font_size = fs
        self.pieces_of_text = []

    def calc_lines(self, text: str):
        """Given the text, figure out where the line should end, delimited by spaces, and return the string split along
        those points

        :param text: A string to be displayed
        :return: List of strings from text split into lines delimited by where it would be too long for the screen
        """
        lines = []
        words = text.split()
        running = ""
        while len(words) > 0:
            while True:
                running = (running + " " + words[0]).strip()
                width = gamebox.from_text(0, 0, running, self.font_size, "white").width
                if width > int(self.background.width) - int(Dialogue.buffer) * 2:
                    running = running[0:len(running) - len(words[0]) - 1]
                    break
                words.pop(0)
                if not words:  # words == []
                    break
            lines.append(running)
            running = ""
        return lines

    def create_text_sprites(self, lines: list):
        """Given lines (hopefully) created by the above method, return gamebox SpriteBoxes to be drawn

        :param lines: List of strings
        :return: Those strings as gameboxes
        """
        height = max([gamebox.from_text(0, 0, line, self.font_size, "white").height for line in lines])
        things = []
        for i in range(len(lines)):
            x = self.background.left
            y = self.background.top
            g = gamebox.from_text(0, 0, lines[i], self.font_size, "black")
            g.x = x + Dialogue.buffer + g.width / 2
            g.y = y + i * (height + Dialogue.buffer) + g.height / 2
            things.append(g)
            self.pieces_of_text.append(g)
        return things

    def update_loc(self, manage_pieces=False):
        a = self.background.left
        self.background.left = camera.left
        a -= self.background.left
        a *= -1

        b = self.background.bottom
        self.background.bottom = camera.bottom
        b -= self.background.bottom
        b *= -1

        if manage_pieces:
            for piece in self.pieces_of_text:
                piece.x += a
                piece.y += b

        return a, b

    def how_much(self, lines: str):
        """A test method to determine how many lines would survive"""
        q = self.calc_lines(lines)
        things = self.create_text_sprites(q)
        count = 0
        for thing in things:
            if thing.bottom < self.background.bottom:
                count += 1
        for thing in things:
            self.pieces_of_text.remove(thing)
        return q[0:count + 1]

    def text_sprites_list(self, lines_list):
        """Does all the work for them!

        :param lines_list: list of lines
        :return: list of created text sprites
        """

        if type(lines_list) == list:
            sprites = []
            for lin in lines_list:
                s = self.create_text_sprites(self.calc_lines(lin))
                sprites.append(s)
            return sprites

        if type(lines_list) == dict:
            sprites = {}
            for key in lines_list.keys():
                s = self.create_text_sprites(self.calc_lines(lines_list[key]))
                sprites[key] = s
            return sprites


def filelocation(file: str, folder: str):
    """Given the file name, get its correct path string depending if folder exists

    :param file: bare file name
    :param folder: optional folder
    :return: the best name for the file
    """
    file_check = re.compile(r"[\\/]?([\w]+[.][\w]+)$")
    file = (file_check.search(file)).groups()[0]
    if Path(folder).is_dir():
        file = folder + "\\" + file
    return file


def file_to_string(file, folder):
    """Gets string from a csv file, stripping extra commas
    Handles file location possibly not being in the maps folder

    :param file: csv file assumed to be in maps (or in base directory if maps doesn't exist)
    :return: string version of file
    """
    text = ""
    #if is_map:
    #    file_type = re.compile(r"(map[\w]+[.]csv)$")
    #else:
    file_type = re.compile(r"[\\/]?([\w]+[.][\w]+)$")
    q = file_type.search(file).groups()[0]
    if q is not None:
        file = filelocation(file, folder)
        try:
            with open(file, 'r') as reader:
                for line in reader:
                    text += line.replace("ï»¿", "").replace("\n", "").strip(",") + "\n"
        except:
            raise Exception("File " + file + " not found in maps, or in base directory if maps doesn't exist")
    else:
        raise Exception("File " + file + " not in correct csv format")
    return text


class Map:
    """It's got everything in one big package"""
    categories = []

    def __init__(self, locations, stuff, tags, dialogue, text, objects, scale, warps):
        self.locations = locations
        self.stuff = stuff
        self.tags = tags
        self.dialogue = dialogue
        self.text = text
        self.objects = objects
        if Map.categories == []:
            Map.categories = open(filelocation("categories.csv", "data"), "r").read().split("\n")
        self.categories = Map.categories
        self.scale = scale
        self.warps = warps
        sort_objects(self)
        self.cool_boxes = self.dialogue.text_sprites_list(self.text)
        print(self.categories)

    def get_list(self, cat_name: str):
        """Get list by name

        :param cat_name:
        :return:
        """
        if (cat_name + "_list") in self.__dict__:
            return self.__dict__[cat_name + "_list"]
        else:
            return None

    def remove(self, thing):
        """Remove thing from all lists

        :param thing:
        :return:
        """
        if thing in self.objects:
            self.objects.remove(thing)
            for cat in self.categories:
                if thing in self.__dict__[str(cat) + "_list"]:
                    self.__dict__[str(cat) + "_list"].remove(thing)


"""This baby's gonna read and write all them damn files so hard, you won't know what hit 'em"""

standard_headers = ["locations", "stuff", "tags", "dialogue", "text", "scale", "categories", "warps"]


def num_or_scale(num, scale: int):
    """
    :param num: Either an integer or "scale"
    :param scale: The value of the scale
    :return: The integer or the value of scale
    """
    return scale if num == "scale" else int(num)


def read_all_data(file: str):
    """Assuming standard map format, reads map related pieces from map file and separates into manageable
    chunks to be handled by further methods

    :param file: File name (assumed to be in maps)
    :return: Dict containing strings of objects in \n format
    """
    text = file_to_string(file, "maps")
    pieces = []
    running = ""
    for line in text.split("\n"):
        if running == "":
            if line.lower().replace(":", "").replace("-", "").strip() in standard_headers:
                running += line.lower().replace(":", "").replace("-", "").strip()
        else:
            if line.lower() == "end":
                pieces.append(running)
                running = ""
            else:
                running += "\n" + line
    dicty = {}
    for piece in pieces:
        key = piece[0:piece.find("\n")]
        val = piece[piece.find("\n") + 1:]
        dicty[key] = val
    return dicty


def read_locations(text):
    """Given a string that holds the numbers as they will appear
    Reads in the information, transposes as required and returns
    a properly formatted list of lists

    :param text: String with numbers in file format
    :return: List of lists of numbers in data format
    """
    lines = []
    for thing in text.split("\n"):
        q = thing.split(",")
        if q != [""]:
            for piece in q:
                if piece == "":
                    piece = 0
            lines.append(q)
    return transpose(lines)


def read_stuff(text: str, scale: int):
    """Given a string holding info for a stuff in file format, create a stuff dict

    :param text: String holding info
    :param scale: handles scale mentions
    :return: dict
    """
    stuff = {}
    for line in text.split("\n"):
        pieces = line.split(",")
        key = pieces[0]
        val = None
        if pieces[1].lower() == "item":
            val = Handler.all_items[pieces[2]]
        elif pieces[1].lower() == "entity":
            val = Handler.all_entities[pieces[2]]
        elif pieces[1].lower() == "spritebox":
            if pieces[2].lower() == "color":
                val = gamebox.from_color(0, 0, pieces[3], num_or_scale(pieces[4], scale),
                                         num_or_scale(pieces[5], scale))
            elif pieces[2].lower() in ["img", "image", "pic"]:
                val = gamebox.from_image(0, 0, filelocation(pieces[3], pieces[4]))
        stuff[key] = val

    return stuff


def read_tags(text):
    """Given a string holding info for a stuff in file format, create a stuff dict

    :param text: String holding info
    :return: dict"""
    tags = {}
    for line in text.split("\n"):
        pieces = line.split(",")
        key = pieces[0]
        val = pieces[1:]
        tags[key] = val
    return tags


def read_dialogue(text):
    """Get the dialogue from the text

    :param text: String holding info
    :return: Dialogue object"""
    parts = text.split(",")
    d = Dialogue(int(parts[0]), int(parts[1]))
    return d


def read_text(text):
    """Get the lines of dialogue from the text

    :param text: String holding info
    :return: dict of strings"""
    keys = []
    vals = []
    for lin in text.split("\n"):
        lin = lin.strip(",")
        key = lin[0:lin.find(",")]
        val = lin[lin.find(",") + 1:]
        keys.append(key)
        vals.append(val)
    all_text = {}
    for i in range(len(keys)):
        all_text[keys[i]] = vals[i]
    return all_text


def read_warps(text):
    """Read the warps

    :param text: String with info
    :return: dict for warps
    """
    warps = {}
    for line in text.split("\n"):
        parts = line.strip(",").split(",")
        warps[parts[0]] = [int(parts[1]), int(parts[2]), int(parts[3])]
    return warps


def read_map_objects(file, w=1, h=1):
    """Get all that work DONE in one method

    :param file: Name of map file
    :param w: multiple of scale
    :param h: multiple of scale
    :return: objects, data
    """
    data = read_all_data(file)
    locations = read_locations(data["locations"])
    scale = int(data["scale"])
    stuff = read_stuff(data["stuff"], scale)
    tags = read_tags(data["tags"])
    add_tags_to_dict(stuff, tags)
    objects = create_map_from_list(locations, stuff, scale * w, scale * h)
    dialogue = read_dialogue(data["dialogue"])
    text = read_text(data["text"])
    warps = read_warps(data["warps"])
    map = Map(locations, stuff, tags, dialogue, text, objects, scale, warps)

    return map
