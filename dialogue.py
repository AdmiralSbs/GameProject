# Watkins, jmw4dx
import gamebox
import pygame


class Dialogue:
    buffer = 5

    def setup(self, h, fs, camera):
        self.background = gamebox.from_color(0, 0, "white", camera.width, h)
        self.background.left = camera.left
        self.background.bottom = camera.bottom
        self.font_size = fs

    def get_max_height(self, lines):
        height = max([gamebox.from_text(0, 0, line, self.font_size, "white").height for line in lines])
        available = self.background.height - Dialogue.buffer * 2
        return max(available - Dialogue.buffer // height, 1)

    def calc_lines(self, text):
        lines = []
        words = text.split()
        running = ""
        while (len(words) > 0):
            # print(len(words))
            while True:
                running = (running + " " + words[0]).strip()
                width = gamebox.from_text(0, 0, running, self.font_size, "white").width
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
        # print(lines)
        return lines

    def create_text_sprites(self, lines):
        height = max([gamebox.from_text(0, 0, line, self.font_size, "white").height for line in lines])
        things = []
        for i in range(len(lines)):
            x = self.background.left
            # print(x)
            y = self.background.top
            g = gamebox.from_text(0, 0, lines[i], self.font_size, "black")
            g.x = x + Dialogue.buffer + g.width / 2
            # print(g.x)
            g.y = y + i * (height + Dialogue.buffer) + g.height / 2
            # print(g.y)
            things.append(g)
        return things

    def update_loc(self, camera, things):
        a = self.background.left
        self.background.left = camera.left
        a -= self.background.left
        a *= -1

        b = self.background.bottom
        self.background.bottom = camera.bottom
        b -= self.background.bottom
        b *= -1

        return (a, b)
