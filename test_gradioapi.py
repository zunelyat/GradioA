# test_gradioapi.py
"""
Tests for GradioAPI module.
"""

import unittest
from gradioapi import GradioAPI

class TestGradioAPI(unittest.TestCase):
    """Test cases for GradioAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GradioAPI()
        self.assertIsInstance(instance, GradioAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GradioAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
