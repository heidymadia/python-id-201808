import unittest
import noob
 
class TestNoob(unittest.TestCase):
 
    def test_mod_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, noob.mod, 1 , 0)

    def test_mod_zero_remainder(self):
        self.assertEqual(0, noob.mod(15,3))
 
if __name__ == '__main__':
    unittest.main()