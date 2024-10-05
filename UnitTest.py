from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__testCases = {
            1: {'prices': [7,1,5,3,6,4], 'output': 5},
            2: {'prices': [7,6,4,3,1], 'output': 0}
        }

        self.__obj = Solution()

        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        prices, output = self.__testCases[1].values()
        result = self.__obj.maxProfit(prices)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        prices, output = self.__testCases[2].values()
        result = self.__obj.maxProfit(prices)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()