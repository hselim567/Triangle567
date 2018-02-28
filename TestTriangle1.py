from Triangle1 import classifyTriangle

import unittest

class TestTriangles(unittest.TestCase):

        
    def test_equal_test(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', "Should be 'Equilateral'")
        
    def test_iso_test(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isosceles', "Should be 'Isosceles'")
    
    def test_right_test(self):
        self.assertEqual(classifyTriangle(4, 3, 5), 'Right', "Should be 'Right'")
        
    def test_scal_test(self):
        self.assertEqual(classifyTriangle(18, 28, 39), 'Scalene', "Should be 'Scalene'")
    
    def test_NotATriangle(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle1', "Should be 'NotATriangle1'")
        
    def test_InvalidInput(self):
        self.assertEqual(classifyTriangle(201, 201, 201), 'InvalidInput1', "Should be 'InvalidInput1'") 
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput2', "Should be 'InvalidInput2'")
        self.assertEqual(classifyTriangle(1.1, 1.1, 1.1), 'InvalidInput3', "Should be 'InvalidInput3'")
        
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()