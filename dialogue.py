# Watkins, jmw4dx
import gamebox


class Dialogue:
    exists = False

    def __init__(self, x, y, w, h):
        if Dialogue.exists: raise Exception("You can only have one Dialogue at a time!")
        background = gamebox.from_color(x, y, "white", w, h)
        lines = []
