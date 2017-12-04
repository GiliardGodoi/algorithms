import unittest as ut
import numpy as np
import random

import sort


class SortTest(ut.TestCase):

    method = None
    array = None
    sortedArray = None 

    @classmethod
    def setUpClass(self):
        arr = np.random.randint(99,high=1000,size=250)
        self.array = list(arr)
        self.array.sort()
        self.sortedArray = list(self.array)

    def setUp(self):
        random.shuffle(self.array)

    def test_insertion_sort(self):
        self.method = sort.InsertionSort()
        arr = self.method.sort(self.array)
        self.assertEqual(arr, self.sortedArray)
    
    def test_select_sort(self):
        self.method = sort.SelectionSort()
        arr = self.method.sort(self.array)
        self.assertEqual(arr, self.sortedArray)

    def test_quick_sort(self):
        self.method = sort.QuickSort()
        arr = self.method.sort(self.array)
        self.assertEqual(arr, self.sortedArray) 

if __name__ == "__main__":
    ut.main()