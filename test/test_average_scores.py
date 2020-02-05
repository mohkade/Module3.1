import unittest
import unittest.mock as mock
from format_output import average_score as topic2


def test_average(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert topic2.average() == 90

if __name__ == '__main__':
    unittest.main()