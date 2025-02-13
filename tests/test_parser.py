import unittest
from parser import test
from constants import FILE_PATHS

class TestJsonParser(unittest.TestCase):
    def test_step1_valid(self):
        print("\nTesting step1 Valid JSON\n")
        test(FILE_PATHS["step1"]["valid"])
        
    def test_step1_invalid(self):
        print("\nTesting step1 Invalid JSON\n")
        with self.assertRaises(Exception):
            test(FILE_PATHS["step1"]["invalid"])
            
    def test_step2_valid(self):
        print("\nTesting step2 Valid JSON\n")
        test(FILE_PATHS["step2"]["valid"])
        
    def test_step2_valid2(self):
        print("\nTesting step2 Valid JSON 2 \n")
        test(FILE_PATHS["step2"]["valid2"])
        
    # def test_step2_invalid(self):
    #     with self.assertRaises(Exception):
    #         test(FILE_PATHS["step2"]["invalid"])
        
    # def test_step2_invalid2(self):
    #     with self.assertRaises(Exception):
    #         test(FILE_PATHS["step2"]["invalid2"])
    
    def test_step3_valid(self):
        print("\nTesting step3 Valid JSON\n")
        test(FILE_PATHS["step3"]["valid"])
        
    def test_step3_invalid(self):
        print("\nTesting step3 Invalid JSON\n")
        with self.assertRaises(Exception):
            test(FILE_PATHS["step3"]["invalid"])
            
    def test_step4_valid(self):
        print("\nTesting step4 Valid JSON\n")
        test(FILE_PATHS["step4"]["valid"])
        
    def test_step4_valid2(self):
        print("\nTesting step4 Valid JSON 2\n")
        test(FILE_PATHS["step4"]["valid2"])
        
    def test_step4_invalid(self):
        print("\nTesting step4 Invalid JSON\n")
        with self.assertRaises(Exception):
            test(FILE_PATHS["step4"]["invalid"])
    

if __name__ == "__main__":
    unittest.main()
