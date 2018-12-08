import unittest
from itertools import repeat

from day3.claim_tree_node import ClaimTreeNode
from day3.claim import Claim
from day3.part_1 import calc_elementary_y_intervals
from tools.segtree import SegmentTree


class TestPart1(unittest.TestCase):
    def setUp(self):
        # All of this comes from the given sample input unless noted
        self.sample_input = (
            ('#1 @ 1,3: 4x4', Claim(1, 1, 3, 1 + 4, 3 + 4)),
            ('#2 @ 3,1: 4x4', Claim(2, 3, 1, 3 + 4, 1 + 4)),
            ('#3 @ 5,5: 2x2', Claim(3, 5, 5, 5 + 2, 5 + 2))
        )
        self.segtree_intervals = (1, 2, 2, 2, 1)
        # Transition sets with expected scores for both thresholds
        self.trans_threshold_1 = ((((2, 3, 1),), 4),
                                  (((1, 2, 1),), 6),
                                  (((2, 3, -1), (3, 3, 1)), 6),
                                  (((1, 2, -1), (3, 3, -1)), 0))
        self.trans_threshold_2 = ((((2, 3, 1),), 0),
                                  (((1, 2, 1),), 2),
                                  (((2, 3, -1), (3, 3, 1)), 0),
                                  (((1, 2, -1), (3, 3, -1)), 0))

    def test_regex(self):
        rect_attrs = ('x1', 'y1', 'x2', 'y2')

        for string, claim2 in self.sample_input:
            claim1 = Claim.from_string(string)

            self.assertEqual(claim1.claim_id, claim2.claim_id)

            for attr in rect_attrs:
                self.assertEqual(getattr(claim1.rect, attr, None), getattr(claim2.rect, attr, None))

    def test_segtree_leaves(self):
        # TOTAL COVERAGE FOR NOW; WILL ADJUST
        # Temp variable until I get conversion logic done

        # Set the threshold to 1 for this test
        ClaimTreeNode.coverage_threshold = 1
        segtree = SegmentTree(tuple(zip(repeat(0), self.segtree_intervals)), ClaimTreeNode)

        # A fresh segment tree with nothing covered shouldn't have a score
        self.assertEqual(segtree.get_score(), 0)

        for tr_set, expected_result in self.trans_threshold_1:
            for transformation in tr_set:
                segtree.update(*transformation)

            self.assertEqual(segtree.get_score(), expected_result)

        # Set the threshold back to 2
        ClaimTreeNode.coverage_threshold = 2

        segtree = SegmentTree(tuple(zip(repeat(0), self.segtree_intervals)), ClaimTreeNode)

        self.assertEqual(segtree.get_score(), 0)

        for tr_set, expected_result in self.trans_threshold_2:
            for transformation in tr_set:
                segtree.update(*transformation)

    def test_y_intervals(self):
        claims = [c[1] for c in self.sample_input]

        self.assertEqual(calc_elementary_y_intervals(claims), self.segtree_intervals)


if __name__ == '__main__':
    unittest.main()
