import unittest
from day3.part_1 import Claim
from tools.segtree.segmenttree import SegmentTree
from tools.segtree.segtree_node import ClaimTreeNode


class TestPart1(unittest.TestCase):
    def setUp(self):
        self.sample = (
            ('#1 @ 1,3: 4x4', Claim(1, 1, 3, 1+4, 3+4)),
            ('#2 @ 3,1: 4x4', Claim(2, 3, 1, 3+4, 1+4)),
            ('#3 @ 5,5: 2x2', Claim(3, 5, 5, 5+2, 5+2))
        )

    def test_regex(self):
        rect_attrs = ('x1', 'y1', 'x2', 'y2')

        for string, claim2 in self.sample:
            claim1 = Claim.from_string(string)

            self.assertEqual(claim1.claim_id, claim2.claim_id)

            for attr in rect_attrs:
                self.assertEqual(getattr(claim1.rect, attr, None), getattr(claim2.rect, attr, None))

    def test_segtree_leaves(self):
        # TOTAL COVERAGE FOR NOW; WILL ADJUST
        # Temp variable until I get conversion logic done
        interval_lengths = ((0, 1), (0, 2), (0, 2), (0, 2), (0, 1))
        transformations = ((((2, 3, 1),), 4),
                           (((1, 2, 1),), 6),
                           (((2, 3, -1), (3, 3, 1)), 6),
                           (((1, 2, -1), (3, 3, -1)), 0))
        segtree = SegmentTree(interval_lengths, ClaimTreeNode)

        # A fresh segment tree with nothing covered shouldn't have a score
        self.assertEqual(segtree.get_score(), 0)

        for tr_set, expected_result in transformations:
            for transformation in tr_set:
                segtree.update(*transformation)

            self.assertEqual(segtree.get_score(), expected_result)

        transformations = ((((2, 3, 1),), 0),
                           (((1, 2, 1),), 2),
                           (((2, 3, -1), (3, 3, 1)), 0),
                           (((1, 2, -1), (3, 3, -1)), 0))

        ClaimTreeNode.coverage_threshold = 2

        segtree = SegmentTree(interval_lengths, ClaimTreeNode)

        self.assertEqual(segtree.get_score(), 0)

        for tr_set, expected_result in transformations:
            for transformation in tr_set:
                segtree.update(*transformation)


if __name__ == '__main__':
    unittest.main()
