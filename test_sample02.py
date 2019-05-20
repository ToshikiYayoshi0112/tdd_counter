import unittest


class TestSample02(unittest.TestCase):
    def test_その1(self):
        self.assertEqual(7, 3 + 4)


if __name__ == "__main__":
    unittest.main()
