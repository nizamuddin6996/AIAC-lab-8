import unittest
from task2 import assign_grade

class TestAssignGrade(unittest.TestCase):
    """Test cases for assign_grade function"""
    
    def test_grade_a_range(self):
        """Test grade A range (90-100)"""
        # Test exact boundary values
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(100), "A")
        
        # Test values within the range
        self.assertEqual(assign_grade(95), "A")
        self.assertEqual(assign_grade(99), "A")
        self.assertEqual(assign_grade(90.5), "A")
        self.assertEqual(assign_grade(99.9), "A")
        
    def test_grade_b_range(self):
        """Test grade B range (80-89)"""
        # Test exact boundary values
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(89), "B")
        
        # Test values within the range
        self.assertEqual(assign_grade(85), "B")
        self.assertEqual(assign_grade(88), "B")
        self.assertEqual(assign_grade(80.1), "B")
        self.assertEqual(assign_grade(89.9), "B")
        
    def test_grade_c_range(self):
        """Test grade C range (70-79)"""
        # Test exact boundary values
        self.assertEqual(assign_grade(70), "C")
        self.assertEqual(assign_grade(79), "C")
        
        # Test values within the range
        self.assertEqual(assign_grade(75), "C")
        self.assertEqual(assign_grade(78), "C")
        self.assertEqual(assign_grade(70.1), "C")
        self.assertEqual(assign_grade(79.9), "C")
        
    def test_grade_d_range(self):
        """Test grade D range (60-69)"""
        # Test exact boundary values
        self.assertEqual(assign_grade(60), "D")
        self.assertEqual(assign_grade(69), "D")
        
        # Test values within the range
        self.assertEqual(assign_grade(65), "D")
        self.assertEqual(assign_grade(68), "D")
        self.assertEqual(assign_grade(60.1), "D")
        self.assertEqual(assign_grade(69.9), "D")
        
    def test_grade_f_range(self):
        """Test grade F range (<60)"""
        # Test values below 60
        self.assertEqual(assign_grade(59), "F")
        self.assertEqual(assign_grade(50), "F")
        self.assertEqual(assign_grade(0), "F")
        self.assertEqual(assign_grade(30), "F")
        self.assertEqual(assign_grade(59.9), "F")
        
    def test_boundary_values(self):
        """Test boundary values between grade ranges"""
        # Boundary between A and B
        self.assertEqual(assign_grade(89.9), "B")
        self.assertEqual(assign_grade(90), "A")
        
        # Boundary between B and C
        self.assertEqual(assign_grade(79.9), "C")
        self.assertEqual(assign_grade(80), "B")
        
        # Boundary between C and D
        self.assertEqual(assign_grade(69.9), "D")
        self.assertEqual(assign_grade(70), "C")
        
        # Boundary between D and F
        self.assertEqual(assign_grade(59.9), "F")
        self.assertEqual(assign_grade(60), "D")
        
    def test_decimal_scores(self):
        """Test decimal score values"""
        # Decimal scores in each grade range
        self.assertEqual(assign_grade(95.7), "A")
        self.assertEqual(assign_grade(87.3), "B")
        self.assertEqual(assign_grade(76.8), "C")
        self.assertEqual(assign_grade(63.2), "D")
        self.assertEqual(assign_grade(45.9), "F")
        
        # Very small decimal values
        self.assertEqual(assign_grade(0.1), "F")
        self.assertEqual(assign_grade(59.99), "F")
        self.assertEqual(assign_grade(89.99), "B")
        
    def test_edge_cases(self):
        """Test edge cases and extreme values"""
        # Zero and negative values
        self.assertEqual(assign_grade(0), "F")
        self.assertEqual(assign_grade(-1), "F")
        self.assertEqual(assign_grade(-10), "F")
        self.assertEqual(assign_grade(-100), "F")
        
        # Very large values
        self.assertEqual(assign_grade(100), "A")
        self.assertEqual(assign_grade(100.0), "A")
        self.assertEqual(assign_grade(100.1), "A")  # Above 100 still gets A
        self.assertEqual(assign_grade(1000), "A")
        self.assertEqual(assign_grade(999999), "A")
        
        # Very small positive values
        self.assertEqual(assign_grade(0.0001), "F")
        self.assertEqual(assign_grade(0.5), "F")
        
    def test_invalid_inputs(self):
        """Test invalid input types and values"""
        # String inputs
        with self.assertRaises(TypeError):
            assign_grade("eighty")
        with self.assertRaises(TypeError):
            assign_grade("95")
        with self.assertRaises(TypeError):
            assign_grade("A")
        with self.assertRaises(TypeError):
            assign_grade("ninety-five")
        
        # Boolean inputs
        with self.assertRaises(TypeError):
            assign_grade(True)
        with self.assertRaises(TypeError):
            assign_grade(False)
        
        # List and tuple inputs
        with self.assertRaises(TypeError):
            assign_grade([90])
        with self.assertRaises(TypeError):
            assign_grade((95,))
        
        # Dictionary inputs
        with self.assertRaises(TypeError):
            assign_grade({"score": 90})
        
        # None input
        with self.assertRaises(TypeError):
            assign_grade(None)
            
    def test_comprehensive_grade_distribution(self):
        """Test comprehensive grade distribution across all ranges"""
        # Test multiple values in each grade range
        grade_a_scores = [90, 91, 95, 99, 100, 90.1, 95.5, 99.9]
        grade_b_scores = [80, 81, 85, 88, 89, 80.1, 85.3, 89.9]
        grade_c_scores = [70, 71, 75, 78, 79, 70.1, 75.7, 79.9]
        grade_d_scores = [60, 61, 65, 68, 69, 60.1, 65.4, 69.9]
        grade_f_scores = [0, 10, 30, 50, 59, 0.1, 30.5, 59.9]
        
        # Verify all A grades
        for score in grade_a_scores:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), "A")
        
        # Verify all B grades
        for score in grade_b_scores:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), "B")
        
        # Verify all C grades
        for score in grade_c_scores:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), "C")
        
        # Verify all D grades
        for score in grade_d_scores:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), "D")
        
        # Verify all F grades
        for score in grade_f_scores:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), "F")

if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)
