class Rect:
    def __init__(self, x1, y1, x2, y2):
        # Top left coords
        self.x1 = x1
        self.y1 = y1

        # Bottom right coords
        self.x2 = x2
        self.y2 = y2

    def intersects(self, other):
        return self.x1 < other.x2 and self.x2 > other.x1 and self.y1 < other.y2 and self.y2 > other.y1
