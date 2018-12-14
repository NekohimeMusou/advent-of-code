import unittest

from day5.part_1 import react_polymer


class Day5Tester(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # (test_input, expected_result
        cls.test_strings = (('aA', ''), ('abBA', ''), ('abAB', 'abAB'),
                            ('aabAAB', 'aabAAB'), ('dabAcCaCBAcCcaDA', 'dabCBAcaDA'))

    def test_polymer_reactions(self):
        for test_input, expected_result in self.test_strings:
            self.assertEqual(expected_result, react_polymer(test_input))
