import unittest

"""
-[ ] 整数値をカウントアップできる
    -[x] 初期値は自由に設定できる
        -[x] 初期値0に設定できる
        -[x] 初期値を15に設定できる
    -[x] カウンターの値を1だけ増やすことができる。
        -[x] 0 -> 1
        -[x] 15 -> 16
    -[x] カウンターの値を増やす幅を自由に決めることができる
        -[x] カウンターの値を2増やすことができる
        -[x] カウンターの値を4増やすことができる
    -[ ] カウントダウンができる
        -[x] カウントの値を1減らすことができる
            -[x] 1 -> 0
            -[x] 14 -> 13
        -[ ] カウンターの値を減らす幅を自由に決めることができる
            -[ ] 15 -> 11
    
"""


class Counter:
    def __init__(self, value):
        self.value = value

    def countup(self, add):
        self.value += add

    def countdown(self, add):
        self.value -= add


class TestCounter(unittest.TestCase):
    def test_カウンターの初期値を0に設定できる(self):
        my_counter = Counter(0)

        self.assertEqual(0, my_counter.value)

    def test_カウンターの初期値を15に設定できる(self):
        my_counter = Counter(15)

        self.assertEqual(15, my_counter.value)

    def test_カウンターの値0から1増やすことができる(self):
        my_counter = Counter(0)

        my_counter.countup(1)

        self.assertEqual(1, my_counter.value)

    def test_カウンターの値を15から16に増やすことができる(self):
        my_counter = Counter(15)

        my_counter.countup(1)

        self.assertEqual(16, my_counter.value)

    def test_カウンターの値を0から2に増やすことができる(self):
        my_counter = Counter(0)

        my_counter.countup(2)

        self.assertEqual(2, my_counter.value)

    def test_カウンターの値を0から4増やすことができる(self):
        my_counter = Counter(0)

        my_counter.countup(4)

        self.assertEqual(4, my_counter.value)

    def test_カウンターの値を1から0に減らすことができる(self):
        my_counter = Counter(1)

        my_counter.countdown(1)

        self.assertEqual(0, my_counter.value)

    def test_カウンターの値を14から13に減らすことができる(self):
        my_counter = Counter(14)

        my_counter.countdown(1)

        self.assertEqual(13, my_counter.value)

    def test_カウンターの値を15から11に減らすことができる(self):
        my_counter = Counter(15)

        my_counter.countdown(4)

        actual = my_counter.value
        expected = 11
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
