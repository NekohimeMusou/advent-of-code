import unittest
from day3.part_1 import Claim


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

    def test_intersect(self):
        claim1, claim2, claim3 = [x[1] for x in self.sample]

        # Sample claims 1 and 2 should intersect
        self.assertTrue(claim1.rect.intersects(claim2.rect))
        self.assertTrue(claim2.rect.intersects(claim1.rect))

        # Sample claim 3 should NOT intersect either 1 or 2
        self.assertFalse(claim1.rect.intersects(claim3.rect))
        self.assertFalse(claim2.rect.intersects(claim3.rect))
        self.assertFalse(claim3.rect.intersects(claim1.rect))
        self.assertFalse(claim3.rect.intersects(claim2.rect))


if __name__ == '__main__':
    unittest.main()
