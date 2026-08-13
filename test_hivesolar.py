# test_hivesolar.py
"""
Tests for HiveSolar module.
"""

import unittest
from hivesolar import HiveSolar

class TestHiveSolar(unittest.TestCase):
    """Test cases for HiveSolar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HiveSolar()
        self.assertIsInstance(instance, HiveSolar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HiveSolar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
