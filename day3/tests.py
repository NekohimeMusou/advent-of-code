import unittest
from day3.part_1 import Claim

SAMPLE_DATA = [
    ('#1 @ 1, 3: 4x4', Claim(1, 1, 3, 1+4, 3+4)),
    ('#2 @ 3,1: 4x4', Claim(2, 3, 1, 3+4, 1+4)),
    ('#3 @ 5,5: 2x2', Claim(3, 5, 5, 5+2, 5+2))
]


class TestPart1(unittest.TestCase):
    def setUp(self):
        self.sample = SAMPLE_DATA

    def test_regex(self):
        test_attrs = ('claim_id', 'x1', 'y1', 'x2', 'y2')

        for string, claim2 in self.sample:
            claim1 = Claim.from_string(string)

            for attr in test_attrs:
                self.assertEqual(getattr(claim1, attr, None), getattr(claim2, attr, None))


if __name__ == '__main__':
    unittest.main()
