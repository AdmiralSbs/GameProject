# Watkins, jmw4dx
import gamebox
import pygame

class Item:
    def __init__(self, name, style, weight, img, color):
        self.name = name
        self.style = style
        self.weight = weight
        if (img != None):
            self.object = gamebox.from_image(0, 0, img)
            color = None
        else:
            if color == None:
                color = 'black'
            self.object = gamebox.from_color(0, 0, color, 50, 50)



class Player:
    def __init__(self, name, move_list, img, color):
        self.name = name
        self.move = move_list
        if (img != None):
            self.object = gamebox.from_image(0, 0, img)
            color = None
        else:
            if color == None:
                color = 'black'
            self.object = gamebox.from_color(0, 0, color, 50, 50)


styles = ["weapon", "potion", "ability"]
names = ['Sean', 'Alexander']
upsorn_moves = ['Piazza Ask', 'Live Code', 'Teach Lecture', 'Wholesome Email']
enemy_moves = ['Vague Answer', 'People\'s United', 'PA Reject', 'LAB DESTROY']

for_loop = Item("FOR_LOOP", 'item', '1', None,)
while_loop = Item('WHILE_LOOP', 'item', '2', None,)
dictionary = Item('DICT', 'item', '3', None,)
list = Item('LIST', 'item', '4', None)
