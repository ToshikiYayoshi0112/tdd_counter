import unittest

"""
-[ ] 整数値をカウントアップできる
    -[ ] 初期値は自由に設定できる
        -[x] 初期値0に設定できる
        -[x] 初期値を15に設定できる
    -[ ] カウントアップは1ずつ
"""


class Counter:
    def __init__(self, value):
        self.value = value


class TestCounter(unittest.TestCase):
    def test_カウンターの初期値を0に設定できる(self):
        my_counter = Counter(0)

        self.assertEqual(0, my_counter.value)

    def test_カウンターの初期値を15に設定できる(self):
        my_counter = Counter(15)

        self.assertEqual(15, my_counter.value)


if __name__ == "__main__":
    unittest.main()
