from abc import ABC, abstractmethod
from itertools import chain


class SegmentTreeNode(ABC):
    @staticmethod
    @abstractmethod
    def create_leaf(value):
        pass

    @staticmethod
    @abstractmethod
    def merge(left, right):
        pass

    @property
    @abstractmethod
    def value(self):
        pass  # This should return something


class SegmentTreeNodeWithUpdate(SegmentTreeNode):
    @abstractmethod
    def update(self, value):
        pass


class ClaimTreeNode(SegmentTreeNodeWithUpdate):
    def __init__(self, value, start, end, children=None):
        self._value = value
        self.start = start
        self.end = end
        self.children = children

    @property
    def value(self):
        return self._value

    @staticmethod
    def create_leaf(value):
        """Create a leaf node with the given value

        value - A tuple like (start, end)"""

        start, end = value

        return ClaimTreeNode(0, start, end)

    @staticmethod
    def merge(left, right):
        """Merge two nodes and return the merged node."""
        start = min(left.start, right.start)
        end = max(left.end, right.end)

        return ClaimTreeNode(0, start, end, (left, right))

    def get_score(self):
        if self.value > 0:
            # The node is a leaf and it's covered by a rectangle
            return self.end - self.start + 1

        if not self.children:
            # If the node's value is 0 and it's a leaf, it's not covered
            return 0

        # If it's 0 and there are children, the score is the sum of its children's scores
        return sum([node.get_score() for node in self.children])

    def update(self, delta):
        """Adjust the value of this node

        delta - +1 or -1 to increment/decrement"""
        self._value += delta
