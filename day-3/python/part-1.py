INPUT_PATH = "../input.txt"
SAMPLE_DATA = ['#1 @ 1, 3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

# grammar: #{CLAIM_ID} @ {X}, {Y}: {W}x{H}


class Claim:
    def __init__(self, x1, y1, x2, y2):
        # Top left coords
        self.x1 = x1
        self.y1 = y1

        # Bottom right coords
        self.x2 = x2
        self.y2 = y2

    @staticmethod
    def from_string(s):
        regex_string = r"^#(\d+)\s*@\s*(\d+),\s*(\d+)\s*:\s*(\d+)x(\d+)"
