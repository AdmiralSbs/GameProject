# Watkins, jmw4dx
import gamebox
import pygame


class Item:
    def __init__(self, name, style, weight, object):
        self.name = name
        self.style = style
        self.weight = weight
        self.object = object


class Player:
    def __init__(self, name, move_list, object):
        self.name = name
        self.move = move_list
        self.object = object


styles = ["weapon", "potion", "ability"]
names = ['Sean', 'Alexander']
upsorn_moves = ['Piazza Ask', 'Live Code', 'Teach Lecture', 'Wholesome Email']
enemy_moves = ['Vague Answer', 'People\'s United', 'PA Reject', 'LAB DESTROY']

for_loop = Item("FOR_LOOP", 'item', '1', gamebox.from_text(0, 0, "FOR", 12, "yellow", bold=True, italic=False))
while_loop = Item('WHILE_LOOP', 'item', '2', None, )
dictionary = Item('DICT', 'item', '3', None, )
list = Item('LIST', 'item', '4', None)
