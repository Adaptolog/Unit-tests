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
    
    def test_delete(self):
        self.cl.append('a')
        self.cl.append('b')
        self.assertEqual(self.cl.delete(1), 'b')
        self.assertEqual(self.cl.length(), 1)
    
    def test_deleteAll(self):
        self.cl.append('a')
        self.cl.append('b')
        self.cl.append('a')
        self.cl.deleteAll('a')
        self.assertEqual(self.cl.length(), 1)
        self.assertEqual(self.cl.get(0), 'b')
    
    def test_get(self):
        self.cl.append('a')
        self.cl.append('b')
        self.assertEqual(self.cl.get(1), 'b')
        with self.assertRaises(IndexError):
            self.cl.get(2)
    
    def test_clone(self):
        self.cl.append('a')
        clone = self.cl.clone()
        clone.append('b')
        self.assertEqual(self.cl.length(), 1)
        self.assertEqual(clone.length(), 2)
    
    def test_reverse(self):
        self.cl.append('a')
        self.cl.append('b')
        self.cl.reverse()
        self.assertEqual(self.cl.get(0), 'b')
        self.assertEqual(self.cl.get(1), 'a')
    
    def test_findFirst(self):
        self.cl.append('a')
        self.cl.append('b')
        self.cl.append('a')
        self.assertEqual(self.cl.findFirst('a'), 0)
        self.assertEqual(self.cl.findFirst('c'), -1)
    
    def test_findLast(self):
        self.cl.append('a')
        self.cl.append('b')
        self.cl.append('a')
        self.assertEqual(self.cl.findLast('a'), 2)
        self.assertEqual(self.cl.findLast('c'), -1)
    
    def test_clear(self):
        self.cl.append('a')
        self.cl.clear()
        self.assertEqual(self.cl.length(), 0)
    
    def test_extend(self):
        list2 = CustomList()
        list2.append('c')
        self.cl.append('a')
        self.cl.extend(list2)
        self.assertEqual(self.cl.length(), 2)
        self.assertEqual(self.cl.get(1), 'c')

if __name__ == '__main__':
    unittest.main()
