import unittest

from day5.common import shortest_reduced_polymer
from day5.part_1 import react_polymer


class Day5Tester(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # (test_input, expected_result
        cls.test_strings = (('aA', ''), ('abBA', ''), ('abAB', 'abAB'),
                            ('aabAAB', 'aabAAB'), ('dabAcCaCBAcCcaDA', 'dabCBAcaDA'))
        cls.reduced_lengths = (('aA', 0), ('abBA', 0), ('abAB', 0), ('aabAAB', 0),
                               ('dabAcCaCBAcCcaDA', 4))

    def test_polymer_reactions(self):
        for test_input, expected_result in self.test_strings:
            self.assertEqual(expected_result, react_polymer(test_input))

    def test_polymer_reductions(self):
        for test_input, min_reduced_length in self.reduced_lengths:
            self.assertEqual(min_reduced_length, shortest_reduced_polymer(test_input))
