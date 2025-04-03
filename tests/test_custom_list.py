import unittest
from custom_list import CustomList

class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.cl = CustomList()
    
    def test_initial_length(self):
        self.assertEqual(self.cl.length(), 0)
    
    def test_append(self):
        self.cl.append('a')
        self.assertEqual(self.cl.length(), 1)
        self.assertEqual(self.cl.get(0), 'a')
    
    def test_insert(self):
        self.cl.insert('a', 0)
        self.cl.insert('b', 1)
        self.cl.insert('c', 1)
        self.assertEqual(self.cl.get(1), 'c')
        with self.assertRaises(IndexError):
            self.cl.insert('d', 4)
    
    # Наступні тести для решти методів
