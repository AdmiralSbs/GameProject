# Watkins, jmw4dx
import gamebox
import pygame


class Dialogue:
    exists = False
    buffer = 5
    font_size = 36

    def setup(self, x, y, w, h, fs):
        if Dialogue.exists:
            raise Exception("You can only have one Dialogue at a time!")
        self.background = gamebox.from_color(x, y, "white", w, h)
        exists = True
        Dialogue.fs = fs

    def get_max_height(self, lines):
        height = max([gamebox.from_text(0, 0, line, Dialogue.font_size, "white").height for line in lines])
        available = self.background.height - Dialogue.buffer * 2
        return max(available // height, 1)

    def calc_lines(self, text):
        lines = []
        words = text.split()
        running = ""
        while (len(words) > 0):
            # print(len(words))
            while True:
                running = (running + " " + words[0]).strip()
                width = gamebox.from_text(0, 0, running, Dialogue.font_size, "white").width
                if width > int(self.background.width) - int(Dialogue.buffer) * 2:
                    l = len(words[0])
                    running = running[0:len(running) - l - 1]
                    break
                words.pop(0)
                # print(words)
                if words == []:
                    break
            lines.append(running)
            running = ""
        return lines

    def create_text_sprites(self, lines):
        print()

d = Dialogue()
d.setup(0, 300, 600, 100, 36)
lyns = d.calc_lines(
    "hello there my dear good friend who needs a shower because you seriously need one my god do you smell")
print(lyns)
print(d.get_max_height(lyns))
