import unittest
import unittest.mock as mock
from format_output import average_score as topic2




class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[2, 2, 2]):
            assert topic2.average(avgNum=2)


if __name__ == '__main__':
    unittest.main()

