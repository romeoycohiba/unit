import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertRaises(TypeError,calc.add(2,'a')) #test if it raises a type error exception if you supply bad arguments. 
        self.assertRaises(TypeError,calc.add(1,2,3)) #test if you get value error when giving 3 arguments instead of 2 to the function. No idea how to implement this atm. 

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-1,1),-2)
        self.assertEqual(calc.subtract(-1,-1),0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-1,1),-1)
        self.assertEqual(calc.multiply(-1,-1),1)
    
'''This part tells me to run the tests above.
Under each class there are defs. Each def is 1 'test'. A def can have multiple checks/test cases.'''
if __name__ == '__main__':
    unittest.main()