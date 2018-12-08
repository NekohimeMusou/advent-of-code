from abc import ABC, abstractmethod


class SegmentTreeNode(ABC):
    @classmethod
    @abstractmethod
    def create_leaf(cls, start, end, value):
        pass

    @classmethod
    @abstractmethod
    def merge(cls, start, end, left, right):
        pass

    @property
    @abstractmethod
    def score(self):
        pass  # This should return something


class SegmentTreeNodeWithUpdate(SegmentTreeNode):
    @abstractmethod
    def update(self, value):
        pass
