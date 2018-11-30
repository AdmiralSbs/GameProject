Checkpoint 2 Relevant Info:
    Thank you so much for reading!  A few things we're looking for in the feedback:
        We did change our idea completely, so anything in terms of how you think it's looking
        Are we hitting the optional requirements already (scrolling / collectibles)?
        How much game are you expecting?  We could honestly just make a few enemies and a few
            things to collect, but if you guys are looking for a game that plays for a good 5 minutes
            then we'll make it happen
        Can we change gamebox to make it better (PLEASE?!?)
            It would allow more flexibility, I've read through it and see weaknesses and ways to make things
            more convenient

    The code is going to be pretty messy because time was ticking and things got bigger.
        Basically, dialogue just makes the white box and the text for it
        Items handles giving SpriteBoxes some extra traits that're cool
        Smartbox handles map building (and will eventually eat up dialogue and items)
        I (jmw4dx) made a change to gamebox (commented out a printish line)

Checkpoint 1 Relevant Info:
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

Our Stuff (read at your pleasure):

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