class Vanish:
    def __init__(self, w, x):
        self.w = w
        self.x = x

    def remove(self):
        c = self.w.replace(self.x, "")
        return c


word= Vanish("space", "s")


print(word.remove())