class SegmentTree:
    def __init__(self, data, node_class):

        self.element_count = len(data)
        self.nodes = {}
        self.node_class = node_class
        self._build_tree(data)

    def get_score(self, low=0, high=None):
        if high is None:
            high = self.element_count - 1

        node = self._get_node_score(1, 0, self.element_count - 1, low, high)
        return node.score

    def update(self, start, end, value):
        self._update(1, start, end, value)

    def _get_node_score(self, tree_index, left, right, low, high):
        if left == low and right == high:
            return self.nodes[tree_index]

        mid = (left + right) / 2

        if low > mid:
            return self._get_node_score(2 * tree_index + 1, mid + 1, right, low, high)

        if high <= mid:
            return self._get_node_score(2 * tree_index, left, mid, low, high)

        left_result = self._get_node_score(2 * tree_index, left, mid, low, mid)
        right_result = self._get_node_score(2 * tree_index + 1, mid + 1, right, mid + 1, high)

        return self.node_class.merge(left_result, right_result)

    def _build_tree(self, data, tree_index=1, start=0, end=None):
        if end is None:
            end = len(data) - 1

        if start == end:
            self.nodes[tree_index] = self.node_class.create_leaf(start, end, data[start])
            return

        left = 2 * tree_index
        right = left + 1
        mid = int((start + end) / 2)

        self._build_tree(data, left, start, mid)
        self._build_tree(data, right, mid + 1, end)
        self.nodes[tree_index] = self.node_class.merge(start, end, self.nodes[left], self.nodes[right])

    def _update(self, tree_index, start, end, value):
        if self.nodes[tree_index].start == self.nodes[tree_index].end:
            self.nodes[tree_index].update(value)
            return

        mid = int((self.nodes[tree_index].start + self.nodes[tree_index].end) / 2)
        left_child_index = 2 * tree_index
        right_child_index = left_child_index + 1

        if start > mid:
            self._update(right_child_index, start, end, value)
        elif end <= mid:
            self._update(left_child_index, start, end, value)
        else:
            self._update(left_child_index, start, mid, value)
            self._update(right_child_index, mid + 1, end, value)

        self.nodes[tree_index] = self.node_class.merge(self.nodes[left_child_index].start,
                                                       self.nodes[right_child_index].end,
                                                       self.nodes[left_child_index],
                                                       self.nodes[right_child_index])
