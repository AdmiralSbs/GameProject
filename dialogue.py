# Watkins, jmw4dx
import gamebox


class Dialogue:
    exists = False
    buffer = 5
    lines = []

    def setup(self, x, y, w, h):
        if Dialogue.exists:
            raise Exception("You can only have one Dialogue at a time!")
        global background
        background = gamebox.from_color(x, y, "white", w, h)
        exists = True

    def run_dialogue(self, text):
        self.calc_lines(text)
        print(Dialogue.lines)

    def calc_lines(self, text):
        words = text.split()
        running = ""
        while (len(words) > 0):
            # print(len(words))
            while True:
                running = (running + " " + words[0]).strip()
                width = gamebox.from_text(0, 0, running, 24, "white").width
                if width > int(background.width) - int(Dialogue.buffer) * 2:
                    l = len(words[0])
                    running = running[0:len(running) - l - 1]
                    break
                words.pop(0)
                # print(words)
                if words == []:
                    break
            Dialogue.lines.append(running)


d = Dialogue()
d.setup(0, 300, 600, 300)
d.run_dialogue("hello")
