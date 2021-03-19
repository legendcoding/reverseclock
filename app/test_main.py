import main
import unittest
from datetime import datetime, timedelta
import random

class TestMain(unittest.TestCase):

    def test_int_valid(self):
        self.assertEqual(main.validation("100"), True)
        self.assertEqual(main.validation("10"), True)
        self.assertEqual(main.validation("1"), True)

    def test_int_not_valid(self):
        self.assertEqual(main.validation("0"), False)
        self.assertEqual(main.validation("-1"), False)
        self.assertEqual(main.validation("-10"), False)
        self.assertEqual(main.validation("-100"), False)

    def test_alpha(self):
        self.assertEqual(main.validation("a"), False)
        self.assertEqual(main.validation("A"), False)
        self.assertEqual(main.validation("a123@#$"), False)
        self.assertEqual(main.validation("@#@!#%^&*("), False)
        self.assertEqual(main.validation("@"), False)
    
    def test_float(self):
        self.assertEqual(main.validation("1.1"), False)
        self.assertEqual(main.validation("0.1"), False)
        self.assertEqual(main.validation("10.1"), False)
        self.assertEqual(main.validation("-10.1"), False)
        self.assertEqual(main.validation("-1.1"), False)
    
    def test_time(self):
        input_secs = 1
        now = datetime.now()
        new_clock = now - timedelta(seconds=input_secs)
        new_clock_time = new_clock.strftime("%H:%M:%S")
        self.assertEqual(main.format_clock(new_clock), new_clock_time)

if __name__ == '__main__':
    unittest.main()


