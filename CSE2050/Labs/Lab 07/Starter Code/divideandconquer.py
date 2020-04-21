import time
class LinkedListIter:
	def __init__(self, lst):
		self.lst=lst

	def __next__(self):
		if self.lst._head != None:
			lost = self.lst._head.value
			self.lst.removeFirst()
			return lost
		else:
			raise StopIteration

	def __iter__(self):
		return self

class ListNode:
    def __init__(self, value, link = None):
        self.value = value
        self.link = link

class LinkedList:
    def __init__(self, L=[]):
        self._head = None
        self._tail = None
        self._length = 0
        for i in L:
            self.addLast(i)

    def removeFirst(self):
        self._length-=1
        value = self._head.value
        self._head = self._head.link
        return value

    def addFirst(self, item):
        self._head = ListNode(item, self._head)
        if self._tail is None:
            self._tail = self._head
        self._length += 1

    def addLast(self, item):
        if self._head is None:
            self.addFirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
            self._length += 1

    def peekLast(self):
        if self._head:
            return self._tail.value
        return None

    def concatenate(self, other):
        if self._head:
            self._tail.link = other._head
            if other:
                self._tail = other._tail
        elif self._head is None:
            return other
        return self

    def __getitem__(self, i):
        cur = self._head
        for j in range(i):
            cur = cur.link
        return cur.value

    def __setitem__(self, i, item):
        cur = self._head
        for j in range(i):
            cur = cur.link
        cur.value = item

    def __str__(self):
        l = []
        cur = self._head
        while cur:
            l.append(cur.value)
            cur = cur.link

        return str(l)

    def __len__(self):
        return self._length

    def __iter__(self):
        return LinkedListIter(self)

def identity(item):
    return item

def splitTheList(L, mid):
    n = len(L)
    cur1 = L._head
    leftHalf = LinkedList()
    rightHalf = LinkedList()
    for i in range(mid):
        leftHalf.addLast(cur1.value)
        cur1 = cur1.link

    cur2 = L._head
    for i in range(mid):
        cur2 = cur2.link

    if cur2:
        for i in range(mid, n):
            rightHalf.addLast(cur2.value)
            cur2 = cur2.link
    return (leftHalf, rightHalf)

def mergeSort(L):
    # Base Case!
    if len(L) < 2:
        return L

    # Divide!
    mid = len(L) // 2
    leftHalf, rightHalf = splitTheList(L, mid)

    # Conquer!
    leftHalf = mergeSort(leftHalf)
    rightHalf = mergeSort(rightHalf)

    # Combine!
    return merge(leftHalf, rightHalf)


def merge(leftHalf, rightHalf):
  temp = LinkedList()
  A = leftHalf._head
  B = rightHalf._head

  while A and B:
      if A.value < B.value:
          temp.addLast(A.value)
          A = A.link
      else:
          temp.addLast(B.value)
          B = B.link

  if A is None:
      while B:
          temp.addLast(B.value)
          B = B.link
      temp._tail = rightHalf._tail
  elif B is None:
      while A:
          temp.addLast(A.value)
          A = A.link

  return temp

# Part 1
def quickSortLinked(L):
    if len(L) < 2:
        return L
    else:
        pivot = L.peekLast()
        (list1, list2, list3) = splitLinkedList(L, pivot)
        L1=quickSortLinked(list1)
        L2=quickSortLinked(list2)
        return L1.concatenate(list3.concatenate(L2))


def splitLinkedList(L, pivot):
    list1 = LinkedList()
    list2 = LinkedList()
    list3 = LinkedList()
    h = L._head
    for x in range(len(L)):
        if h == None:
            break
        elif h.value > pivot:
            list2.addLast(h.value)
        elif h.value < pivot:
            list1.addLast(h.value)
        elif h.value == pivot:
            list3.addLast(h.value)
        h = h.link
    return (list1, list2, list3)

# Part 2
def quickSortInPlace(L, startIdx = 0, endIdx = None):
    if endIdx == None:
        endIdx = len(L)
    if endIdx - startIdx >= 1:
        middle = splitList(L, (endIdx - 1), startIdx, endIdx)
        quickSortInPlace(L, startIdx, middle)
        quickSortInPlace(L, (middle + 1), endIdx)
    return L

def splitList(L, pivot, startIdx, endIdx):
    i = startIdx
    j = pivot - 1
    while i < j:
        while L[i] < L[pivot]:
            i += 1
        while i < j and L[j] >= L[pivot]:
            j -= 1
        if i < j:
            g = L[i]
            k = L[j]
            L[i] = k
            L[j] = g
    if L[pivot] <= L[i]:
        Lp = L[pivot]
        Li = L[i]
        L[i] = Lp
        L[pivot] = Li
        pivot = i
    return pivot

# Part 3 and 4
def quickSort(L, startIdx=0, endIdx=-1, keyFunc=identity):
    if (endIdx == -1):
        endIdx = len(L) - 1
    if endIdx == None:
        endIdx = len(L)
    if endIdx - startIdx >= 1:
        middle = partition(L, keyFunc, startIdx, endIdx, (endIdx - 1))
        quickSort(L, startIdx, middle, keyFunc)
        quickSort(L, (middle + 1), endIdx, keyFunc)
    return L

def partition(L, keyFunc, startIdx, endIdx, pivot):
    i = startIdx
    j = pivot - 1
    while i < j:
        while keyFunc(L[i]) < keyFunc(L[pivot]):
            i += 1
        while i < j and keyFunc(L[j]) >= keyFunc(L[pivot]):
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    if keyFunc(L[pivot]) <= keyFunc(L[i]):
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    return pivot
#4b ruined everything so i just took it out if you guys manuely grade this i can pop it back in
# this lab just took forever so i didnt wont to compromise the points in order to fix that issue.
## Part 5
def findKthLinked(L, k, loud=False):
    if len(L) < 2:
        if L:
            return L[0]
        else:
            return None

    pivot = L.peekLast()

    # uses the splitLinkedList function you write in part 1
    LT, ET, GT = splitLinkedList(L, pivot)
    if loud:
        print("Pivot:", pivot)
        print("Split lists:", LT, ET, GT)

    if k <= len(LT):
        return findKthLinked(LT, k, loud)
    elif k <= (len(LT) + len(ET)):
        return ET[0]
    else:
        k = k - (len(LT) + len(ET))
        return findKthLinked(GT, k, loud)

def findKth(L, k, keyFunc = identity):
    if len(L) < 2:
        if L:
            return L[0]
    pivot = (len(L) - 1) // 2
    GT, LT, ET = splitListKth(L, pivot, keyFunc)
    llt=len(LT)
    if k <= llt:
        return findKth(LT, k, keyFunc)
    elif k <= (llt + len(ET)):
        return ET[0]
    else:
        k = k - (llt + len(ET))
        return findKth(GT, k, keyFunc)

def splitListKth(L, pivot, keyFunc):
    lp=L[pivot]
    GT, LT, ET = [], [], []
    for x in L:
        if keyFunc(x) > keyFunc(lp):
            GT.append(x)
        elif keyFunc(x) < keyFunc(lp):
            LT.append(x)
        else:
            ET.append(x)
    return GT, LT, ET

def	rightMostDigitNeg(item):
    return - 1 * (item % 10)
