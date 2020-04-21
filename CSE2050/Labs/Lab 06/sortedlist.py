from random import randint
class SortedList:
	def __init__(self, L = [], cmpIn = None):
		self._cmp = cmpIn
		self._L = L
		self.ctComparisons = 0
		self.selectionSort()
	# Selection sort provided to you
	def selectionSort(self):
		self.ctComparisons = 0
		for i in range(len(self._L)):
			min_idx = i
			for j in range(i+1, len(self._L)):
				if self._compare(self._L[min_idx], self._L[j]) == 1:
					min_idx = j
			self._L[i], self._L[min_idx] = self._L[min_idx], self._L[i]
		return self.ctComparisons

	def add(self, item):
		self.ctComparisons = 0
		if len(self._L) == 0:
			self._L.append(item)
			return
		for x in range(len(self._L)):
			if self._compare(self._L[x], item) == 1:
				return self._L.insert(x, item)
			else:
				pass
		return self._L.append(item)
		return self.ctComparisons

	def _compare(self, i, j):
		self.ctComparisons += 1
		if self._cmp != None:
			return self._cmp(i, j)
		else:
			if i > j:
				return 1
			elif i == j:
				return 0
			else:
				return -1

	def setComparison(self, cmpFunction):
		self._cmp = cmpFunction
		self.selectionSort()

	def helper(self, L):
		if len(L) == 1:
			return
		mid = len(L) // 2
		x = L[:mid]
		y = L[mid:]
		self.helper(x)
		self.helper(y)
		self.merge(x, y, L)

	def mergeSort(self, L):
		self.ctComparisons = 0
		self.helper(L)

	def merge(self, A, B, L):
		x = 0
		y = 0
		while x < len(A) and y < len(B):
			if self._compare(A[x], B[y]) == -1:
				L[x + y] = A[x]
				x += 1
			else:
				L[x + y] = B[y]
				y += 1
		L[x + y:] = A[x:] + B[y:]

	def __contains__(self, item):
		self.ctComparisons = 0
		left = 0
		right = len(self._L)
		while right >= left:
			mid = (left + right)  // 2
			if self._compare(self._L[mid], item) == 0:
				return True
			elif self._compare(self._L[mid], item) == 1:
				left = mid + 1
			elif self._compare(self._L[mid], item) == -1:
				right = mid -1
			return False

	def __str__(self):
		strng = ""
		for x in self._L:
			strng += str(x)
			strng += ","
		return strng.strip(",")

## DO NOT modify these functions. They are the comparison functions for testing purposes.

def cmpBySum(i, j):
    sum1 = 0
    sum2 = 0
    while i > 0:
        d = i%10
        i = i//10
        sum1 += d
    while j > 0:
        d = j%10
        j = j//10
        sum2 += d
    if sum1 < sum2:
        return -1
    elif sum1 == sum2:
        return 0
    else:
        return 1

def ageCmp(i, j):
	i = i[2]
	j = j[2]
	if i < j:
		return -1
	elif i == j:
		return 0
	else:
		return 1

def nameCmp(x, y):
	x = x[1]
	y = y[1]
	n = min(len(x), len(y))
	for i in range(n):
		if x[i] < y[i]:
			return -1
		elif x[i] > y[i]:
			return 1
		elif i == n-1 and x[i] == y[i]:
			return 0

def stringLenCmp(x, y):
	if len(x) < len(y):
		return -1
	elif len(x) == len(y):
		return 0
	else:
		return 1
L=[9, 8, 7, 6]
sl =SortedList(L)
print(sl.ctComparisons)
print(sl)
sl.mergeSort(L)
print(sl)
print(sl.ctComparisons)
L =	[i for	i in range(500)]
sl.mergeSort(L)
print(sl.ctComparisons)
sl = SortedList(L)
sl.mergeSort(L)
print(sl.ctComparisons)
def testPerformance(n):
	pass
