List of lists format for processing:
    Each minor list in the major list contains the data for one column (x value)
    Each item in the minor list contains the data for one cell in that column
    For each item in the minor list, the y value increments
    For each minor list in the major list, the x value increments
    The filling goes from top to bottom, then from left to right
    Not every spot going down needs to be filled with data

So you want to mess around with it:
    Create or edit the map file
    Edit the dictionary
    Should work just fine



0) greeting
1) averages
2) higher_lower_player
3) str_redux
4) lou's list
5) regex

BASIC CODE
FUNCTIONS
LOOPS
DATA STRUCTURES (LIST/DICT)
READ FILE/INTERNET
REGEX

Basic Storyline:

Upsorn (Player) trapped in Archimedes Server
    Archimedes Server:
        Piazza:
        CS 1110:
    Gains Tools and Potions to help
        Tools: For Loops, While Loops, Dicts, Lists
        Potions: Piazza Answers

Moves:
    Upsorn's Moves:
        Ask Question on Piazza
        Live Coding Session
        Show Up to Lecture
        Send a wholesome email
    TA's Moves:
        Give Vague Answer to Piazza Question
        WE ARE PEOPLE TOO
        Bogus PA Test Case
        Make In-Class Lab Harder at 3:12pm



"""
A sample of what a map could look like (made in program)
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
"""