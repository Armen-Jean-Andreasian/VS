# unit_tests/pairing.py
import unittest
from shared_scripts.pairs.pairing import MakePairs


class TestMakePairs(unittest.TestCase):
    def test_non_empty_input(self):
        test_one = MakePairs(["Real Madrid", "Barcelona", "Chelsea", "Liverpool"]).get_pairs()
        self.assertTrue(test_one)
        self.assertGreater(test_one.__len__(), 0)

    def test_empty_input(self):
        with self.assertRaises(SyntaxError):
            MakePairs([]).get_pairs()


if __name__ == '__main__':
    unittest.main()
