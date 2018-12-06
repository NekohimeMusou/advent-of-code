import re

INPUT_PATH = "input.txt"

# grammar: #{CLAIM_ID} @ {X}, {Y}: {W}x{H}


class Claim:
    def __init__(self, claim_id, x1, y1, x2, y2):
        self.claim_id = claim_id

        # Top left coords
        self.x1 = x1
        self.y1 = y1

        # Bottom right coords
        self.x2 = x2
        self.y2 = y2

    regex = re.compile(r"#\s*(\d+)\s*@\s*(\d+),\s*(\d+)\s*:\s*(\d+)\s*x\s*(\d+)")

    @classmethod
    def from_string(cls, s):
        match = cls.regex.match(s)

        if match:
            claim_id, x1, y1, w, h = [int(x) for x in match.groups()]
            x2 = x1 + w
            y2 = y1 + h

            return Claim(claim_id, x1, y1, x2, y2)

        return None
