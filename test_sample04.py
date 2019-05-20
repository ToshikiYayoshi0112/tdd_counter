import unittest

"""
-[ ] 2つの整数の四則演算をできるようにする
    -[x] 和
        -[x] 3 + 4 = 7
        -[x] 2 + 3 = 5
    -[x] 差
    -[ ] 積
    -[ ] 商
"""


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


class TestCalculation(unittest.TestCase):
    def test_2つの整数の和を計算できる_3足す4は7(self):
        # 3 + 4をする関数をデザインする
        self.assertEqual(7, add(num1=3, num2=4))

    def test_2つの整数の和を計算できる_2足す3は5(self):
        # 2 + 3をする関数をデザインする
        self.assertEqual(5, add(num1=2, num2=3))

    def test_2つの整数の差を計算できる_5引く2は3(self):
        # 5 - 2 をする関数をデザイン
        self.assertEqual(3, sub(num1=5, num2=2))

    def test_2つの整数の差を計算できる_4引く8はマイナス4(self):
        # 4 − 8をする関数をデザイン
        self.assertEqual(-4, sub(num1=4, num2=8))


if __name__ == "__main__":
    unittest.main()
