class TreeTransformation:
    def __init__(self, x, y1, y2, delta):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.delta = delta

    def as_tuple(self):
        return self.y1, self.y2, self.delta
