# Watkins, jmw4dx
import gamebox
import pygame


def make_item(self, name, style, weight):
    self.name = name
    self.style = style
    self.weight = weight


def make_player(self, name, move_list, inventory, health):
    self.name = name
    self.move_list = move_list
    self.inventory = inventory
    self.health = health


styles = ["weapon", "potion", "ability"]
names = ['Sean', 'Alexander']
upsorn_moves = ['Piazza Ask', 'Watch Live Code', 'Attend Lecture', 'Wholesome Email']
enemy_moves = ['Vague Answer', 'We\'re people too', 'PA Reject', 'LAB DESTROY']

for_loop = gamebox.from_text(0, 0, "FOR", 12, "yellow", bold=True, italic=False)
make_item(for_loop, "FOR_LOOP", 'item', '1')
while_loop = gamebox.from_text(0, 0, "WHILE", 12, "red", bold=True, italic=False)
make_item(while_loop, 'WHILE_LOOP', 'item', '2')
dictionary = gamebox.from_text(0, 0, "DICT", 12, "lightblue", bold=True, italic=False)
make_item(dictionary, 'DICT', 'item', '3')
list = gamebox.from_text(0, 0, "LIST", 12, "gray", bold=True, italic=False)
make_item(list, "LIST", 'item', '4')

# enemy1 = Player('Bob', enemy_moves, gamebox.from_color(0, 0, 'red', 10, 10), None, 50)
enemy1 = gamebox.from_color(0, 0, 'red', 10, 10)
make_player(enemy1, 'Bob', enemy_moves, [], 50)
upsorn = gamebox.from_color(0, 0, 'yellow', 10, 10)
make_player(upsorn, 'upsorn', upsorn_moves, [], 50)

inventory = []
