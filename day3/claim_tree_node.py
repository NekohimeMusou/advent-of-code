from tools.segtree import SegmentTreeNodeWithUpdate


class ClaimTreeNode(SegmentTreeNodeWithUpdate):
    coverage_threshold = 2

    def __init__(self, start, end, coverage, length, children=None, score=None):
        self._coverage = coverage
        self.length = length
        self.children = children
        self.start = start
        self.end = end

        if score is None:
            self._score = self._calc_leaf_score()
        else:
            self._score = score

    @property
    def score(self):
        return self._score

    @property
    def coverage(self):
        return self._coverage

    @classmethod
    def create_leaf(cls, start, end, value):
        """Create a leaf node with the given value

        value - (rectangles_covering_leaf, length_of_line_segment)"""

        coverage, length = value

        return cls(start, end, coverage, length)

    @classmethod
    def merge(cls, start, end, left, right):
        """Merge two nodes and return the merged node.

        Obviously, merged nodes are never leaves"""

        if left.coverage != right.coverage:
            coverage = 0
        else:
            coverage = left.coverage

        score = left.score + right.score

        return cls(start, end, coverage, left.length+right.length, score=score, children=(left, right))

    def update(self, delta):
        """Adjust the value of this node.

        delta - +1 or -1 to increment/decrement"""
        self._coverage += delta

        self._score = self._calc_leaf_score()

    def _calc_non_leaf_score(self):
        if self._coverage > 0:
            return self.length
        else:
            return sum([node.score for node in self.children])

    def _calc_leaf_score(self):
        if self._coverage >= self.coverage_threshold:
            return self.length

        return 0
