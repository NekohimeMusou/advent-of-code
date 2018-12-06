import re

INPUT_PATH = "input.txt"

# grammar: #{CLAIM_ID} @ {X}, {Y}: {W}x{H}


def main():
    claim_list = get_input()

    # http://tryalgo.org/en/geometry/2016/06/25/union-of-rectangles/
    # https://cp-algorithms.com/data_structures/segment_tree.html
    # https://kartikkukreja.wordpress.com/2014/11/09/a-simple-approach-to-segment-trees/

    # First, divide into y-intervals
    # Then sweep line from left; when line touches the left side of a rect, increment counter(s) for its interval
    # When line leaves the right side, decrement the counter


def get_input(path=INPUT_PATH):
    with open(path) as f:
        lines = [Claim.from_string(line) for line in f]

    # Invalid lines (blanks) will be None so filter them out
    return [claim for claim in lines if claim is not None]


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


class Claim:
    def __init__(self, claim_id, x1, y1, x2, y2):
        self.claim_id = claim_id

        self.rect = Rect(x1, y1, x2, y2)

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


if __name__ == '__main__':
    main()
