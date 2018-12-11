import unittest
from itertools import repeat

from day3.claim_tree_node import ClaimTreeNode
from day3.claim import Claim
from day3.part_1 import calc_elementary_y_intervals, generate_sweep_events, calculate_overlap, \
    find_segtree_interval
from day3.part_2 import find_non_overlapping_claim
from tools.segtree import SegmentTree


class TestPart1(unittest.TestCase):
    def setUp(self):
        # All of this comes from the given sample input unless noted
        self.sample_input = (
            ('#1 @ 1,3: 4x4', Claim(1, 1, 3, 1 + 4, 3 + 4)),
            ('#2 @ 3,1: 4x4', Claim(2, 3, 1, 3 + 4, 1 + 4)),
            ('#3 @ 5,5: 2x2', Claim(3, 5, 5, 5 + 2, 5 + 2))
        )
        self.claims = [c[1] for c in self.sample_input]
        self.sweep_events = {1: [(2, 3, 1)],
                             3: [(1, 2, 1)],
                             5: [(2, 3, -1), (3, 3, 1)],
                             7: [(1, 2, -1), (3, 3, -1)]}
        # The last segment was always blank. Changing this from (1, 2, 2, 2, 1) and removing
        # the code that added the last interval, all unit tests still pass
        self.segtree_intervals = (1, 2, 2, 2)
        self.rectangle_y_intervals = (((3, 7), (2, 3)),
                                      ((1, 5), (1, 2)),
                                      ((5, 7), (3, 3)))
        # Transition sets with expected scores for both thresholds
        transition_set = (((2, 3, 1),),
                          ((1, 2, 1),),
                          ((2, 3, -1), (3, 3, 1)),
                          ((1, 2, -1), (3, 3, -1)))
        self.trans_threshold_1 = zip(transition_set, (4, 6, 6, 0))
        self.trans_threshold_2 = zip(transition_set, (0, 2, 0, 0))

    def test_regex(self):
        rect_attrs = ('x1', 'y1', 'x2', 'y2')

        for string, claim2 in self.sample_input:
            claim1 = Claim.from_string(string)

            self.assertEqual(claim1.claim_id, claim2.claim_id)

            for attr in rect_attrs:
                self.assertEqual(getattr(claim2.rect, attr, None), getattr(claim1.rect, attr, None))

    def test_segtree_leaves(self):
        # Set the threshold to 1 for this test
        ClaimTreeNode.coverage_threshold = 1
        segtree = SegmentTree(list(zip(repeat(0), self.segtree_intervals)), ClaimTreeNode)

        # A fresh segment tree with nothing covered shouldn't have a score
        self.assertEqual(0, segtree.get_score())

        for tr_set, expected_result in self.trans_threshold_1:
            for transformation in tr_set:
                segtree.update(*transformation)

            self.assertEqual(expected_result, segtree.get_score())

        # Set the threshold back to 2
        ClaimTreeNode.coverage_threshold = 2

        segtree = SegmentTree(tuple(zip(repeat(0), self.segtree_intervals)), ClaimTreeNode)

        self.assertEqual(0, segtree.get_score())

        for tr_set, expected_result in self.trans_threshold_2:
            for transformation in tr_set:
                segtree.update(*transformation)

            self.assertEqual(expected_result, segtree.get_score())

    def test_elementary_y_intervals(self):
        self.assertEqual(self.segtree_intervals, calc_elementary_y_intervals(self.claims))

    def test_sweep_events(self):
        events = generate_sweep_events(self.claims, self.segtree_intervals)

        self.assertEqual(self.sweep_events, events)

    def test_tree_sweep(self):
        total_score = calculate_overlap(self.segtree_intervals, self.sweep_events)

        self.assertEqual(4, total_score)

    def test_rectangle_y_intervals(self):
        for rect_interval, expected in self.rectangle_y_intervals:
            self.assertEqual(expected, find_segtree_interval(self.segtree_intervals, rect_interval))


class TestPart2(unittest.TestCase):
    def setUp(self):
        self.claims = {1: Claim(1, 1, 3, 1 + 4, 3 + 4),
                       2: Claim(2, 3, 1, 3 + 4, 1 + 4),
                       3: Claim(3, 5, 5, 5 + 2, 5 + 2)}
        self.expected_unique_claim = 3

    def test_intersect(self):
        # Each claim should intersect itself
        for claim in self.claims.values():
            self.assertTrue(claim.intersects(claim))

        # Claim 1 should intersect 2 but not 3
        self.assertTrue(self.claims[1].intersects(self.claims[2]))
        self.assertFalse(self.claims[1].intersects(self.claims[3]))

        # Claim 2 should intersect 1 but not 3
        self.assertTrue(self.claims[2].intersects(self.claims[1]))
        self.assertFalse(self.claims[2].intersects(self.claims[3]))

        # Claim 3 should not intersect either other one
        self.assertFalse(self.claims[3].intersects(self.claims[1]))
        self.assertFalse(self.claims[3].intersects(self.claims[2]))

    def test_claim_finder(self):
        self.assertEqual(self.expected_unique_claim, find_non_overlapping_claim(self.claims))


if __name__ == '__main__':
    unittest.main()
