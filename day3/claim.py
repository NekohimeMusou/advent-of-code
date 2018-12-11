import re

from day3.rect import Rect


class Claim:
    def __init__(self, claim_id, x1, y1, x2, y2):
        self.claim_id = claim_id

        self.rect = Rect(x1, y1, x2, y2)

    def intersects(self, other):
        return self.rect.intersects(other.rect)

    regex = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

    @classmethod
    def from_string(cls, s):
        match = cls.regex.match(s)

        if match:
            claim_id, x1, y1, w, h = [int(x) for x in match.groups()]
            x2 = x1 + w
            y2 = y1 + h

            return Claim(claim_id, x1, y1, x2, y2)

        return None
