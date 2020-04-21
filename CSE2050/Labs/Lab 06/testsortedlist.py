import unittest
from random import randint
from sortedlist import *

class TestLinkedList(unittest.TestCase):

    def testsetcomparison(self):
        sl = SortedList([])
        self.assertEqual(sl._cmp, None)
        sl.setComparison(cmpBySum)
        self.assertEqual(sl._cmp, cmpBySum)

    def testaddint(self):
        sl = SortedList([])
        
        sl.add(123)
        self.assertEqual(sl.ctComparisons, 0)
        
        sl.add(34)
        self.assertEqual(sl.ctComparisons, 1)

        sl.add(26)
        self.assertEqual(sl.ctComparisons, 1)

        sl.add(9)
        self.assertEqual(sl.ctComparisons, 1)

        sl.add(999)
        self.assertEqual(sl.ctComparisons, 4)

        self.assertEqual(sl._L, [9, 26, 34, 123, 999])

    def testaddtuples(self):
        l_id = [(1, 'Amy', 18), (2, 'Jessica', 19), (3, 'Becky', 20), (4, 'Harry', 17), (5, 'Tom', 16), (6, 'Ben', 21), (7, 'Amy', 10)]
        sl = SortedList([])

        sl.add((2, 'Jessica', 19))
        self.assertEqual(sl.ctComparisons, 0)

        sl.add((6, 'Ben', 21))
        self.assertEqual(sl.ctComparisons, 1)

        sl.add((4, 'Harry', 17))
        self.assertEqual(sl.ctComparisons, 2)

        sl.add((3, 'Becky', 20))
        self.assertEqual(sl.ctComparisons, 2)

        sl.add((1, 'Amy', 18))
        self.assertEqual(sl.ctComparisons, 1)

        sl.add((5, 'Tom', 16))
        self.assertEqual(sl.ctComparisons, 5)

        sl.add((7, 'Amy', 10))
        self.assertEqual(sl.ctComparisons, 6)

        self.assertEqual(sl._L, l_id)

        l_name = [(1, 'Amy', 18), (7, 'Amy', 10), (3, 'Becky', 20), (6, 'Ben', 21), (4, 'Harry', 17), (2, 'Jessica', 19), (5, 'Tom', 16)]
        sl = SortedList([(1, 'Amy', 18), (2, 'Jessica', 19), (3, 'Becky', 20), (4, 'Harry', 17), (5, 'Tom', 16), (6, 'Ben', 21), (7, 'Amy', 10)], nameCmp)
        self.assertEqual(sl._L, l_name)
        self.assertEqual(sl.ctComparisons, 21)

        l_age = [(7, 'Amy', 10), (5, 'Tom', 16), (4, 'Harry', 17), (1, 'Amy', 18), (2, 'Jessica', 19), (3, 'Becky', 20), (6, 'Ben', 21)]
        sl = SortedList([(1, 'Amy', 18), (7, 'Amy', 10), (3, 'Becky', 20), (6, 'Ben', 21), (4, 'Harry', 17), (2, 'Jessica', 19), (5, 'Tom', 16)], ageCmp)
        self.assertEqual(sl._L, l_age)
        self.assertEqual(sl.ctComparisons, 21)

    def testsetgenericcompare(self):
        sl = SortedList([123, 34, 26, 9])
        sl.setComparison(cmpBySum)
        self.assertEqual(sl._L, [123, 34, 26, 9])

        l_name = [(1, 'Amy', 18), (7, 'Amy', 10), (3, 'Becky', 20), (6, 'Ben', 21), (4, 'Harry', 17), (2, 'Jessica', 19), (5, 'Tom', 16)]
        l_id = [(1, 'Amy', 18), (2, 'Jessica', 19), (3, 'Becky', 20), (4, 'Harry', 17), (5, 'Tom', 16), (6, 'Ben', 21), (7, 'Amy', 10)]
        sl = SortedList(l_id)
        sl.setComparison(nameCmp)
        self.assertEqual(sl._L, l_name)

        l_age = [(7, 'Amy', 10), (5, 'Tom', 16), (4, 'Harry', 17), (1, 'Amy', 18), (2, 'Jessica', 19), (3, 'Becky', 20), (6, 'Ben', 21)]
        sl = SortedList(l_id)
        sl.setComparison(ageCmp)
        self.assertEqual(sl._L, l_age)

    def teststrings(self):
        sl = SortedList(["Banana", "Candy", "Coconut", "Beetroot"], stringLenCmp)
        self.assertEqual(sl._L, ["Candy", "Banana", "Coconut", "Beetroot"])
        self.assertEqual(sl.ctComparisons, 6)

    def testcontains(self):
        sl = SortedList([6, 33, 11, 45, 8, 1, 34])
        test = 11 in sl
        self.assertEqual(sl.ctComparisons, 1)

        sl1 = SortedList(["Banana", "Candy", "Coconut", "Beetroot"], stringLenCmp)
        test = "Beetroot" in sl1
        self.assertEqual(sl1.ctComparisons, 3)

        sl2 = SortedList([(1, 'Amy', 18), (2, 'Jessica', 19), (3, 'Becky', 20), (4, 'Harry', 17), (5, 'Tom', 16), (6, 'Ben', 21), (7, 'Amy', 10)])
        test = (2, 'Jessica', 19) in sl2
        self.assertEqual(sl2.ctComparisons, 2)

    def testmergesort(self):
        sl = SortedList([22, 20, 12, 2, 4, 6, 4, 2, 0, -1, -3])
        self.assertEqual(sl.ctComparisons, 55)

        sl.mergeSort(sl._L)
        self.assertEqual(sl.ctComparisons, 18)

        sl = SortedList([4, 10, -20, -3, 5, 8, 2, 2])
        self.assertEqual(sl.ctComparisons, 28)

        sl.mergeSort(sl._L)
        self.assertEqual(sl.ctComparisons, 12)

        sl = SortedList([6, 8, -2, 0, 1, -6])
        self.assertEqual(sl.ctComparisons, 15)

        sl.mergeSort(sl._L)
        self.assertEqual(sl.ctComparisons, 7)

        sl = SortedList([10])
        self.assertEqual(sl.ctComparisons, 0)

        sl.mergeSort(sl._L)
        self.assertEqual(sl.ctComparisons, 0)


if __name__ == "__main__":
    unittest.main()

