class LinkedListIter:
	def __init__(self, lst):
		self.lst=lst

	def __next__(self):
		if self.lst._head != None:
			lost=self.lst._head.value
			self.lst.removeFirst()
			return lost
		else:
			raise StopIteration

	def __iter__(self):
		return self

class LinkedList:
	class _Node:
		def __init__(self, value, link = None):
			self.value=value
			self.link=link
	def sillytest(self):
		self._head=self._Node("foo")
		print(self._head.value)

	def __init__(self, nodeCount=0):
		self._head=None
		self._tail=None
		self._nodeCount=nodeCount
	def addFirst(self, item):
		self._nodeCount+=1
		newnode=LinkedList._Node(item)
		if self._head == None:
			self._head=LinkedList._Node(item)
			self._tail=self._head
			self._head.link=None
		else:
			newnode.link=self._head
			self._head=newnode
	def addLast(self, item):
		self._nodeCount+=1
		node=LinkedList._Node(item)
		if self._tail == None:
			self._head=node
			self._tail= node
			self._tail.link=None
			self._head.link=None
		else:
			self._tail.link=node
			self._tail=node

	def removeFirst(self):
		self._nodeCount-=1
		value=self._head.value
		self._head=self._head.link
		return value

	def append(self, other):
		if self._nodeCount == 0 and other._nodeCount != 0:
			self._tail = other._tail
			self._head = other._head
			self._nodeCount = other._nodeCount
		elif other._nodeCount != 0:
			self._tail.link = other._head
			self._tail = other._tail
			self._nodeCount += other._nodeCount
		other._nodeCount = 0
		other._tail = None
		other._head = None

	def removeLast(self):
		self._nodeCount-=1
		node=self._head
		while node.link != self._tail:
			node = node.link
		node.link=None
		self._tail = node

	def addAt(self, i, item):
		newnode=LinkedList._Node(item)
		self._nodeCount+=1
		if i == 0:
			self.addFirst(item)
		elif i == self._nodeCount:
			self.addLast(item)
		else:
			temp = 0
			latest = self._head
			while temp < (i-1):
				latest = latest.link
				temp += 1
			zero = latest.link
			latest.link = newnode
			newnode.link = zero
			self._tail = zero


	def removeAt(self, i):
		self._nodeCount-=1
		if i ==0:
			self.removeFirst()
		elif i == self._nodeCount:
			self.removeLast()
		else:
			temp = 0
			latest = self._head
			while temp < (i-1):
				latest=latest.link
				temp += 1
			negone=latest.link
			zero=negone.link
			negtwo=negone.link
			negone.link=negtwo


	def __str__(self):
		strng=[]
		n=self._head
		while n!= None:
			strng.append(str(n.value))
			n=n.link
		return "[" + ";".join(strng) + "]"

	def __getitem__(self, i):
		node=self._head
		sum = 0
		if i >= self._nodeCount:
			raise Exception("Invalid" + str(i))
		else:
			while sum != i:
				node = node.link
				sum+=1
			return node.value

	def __setitem__(self, i, item):
		node=self._head
		sum = 0
		if i >= self._nodeCount:
			raise Exception("Try again LOL" + str(i))
		else:
			while sum != i:
				node = node.link
				sum+=1
			node.value=item

	def __contains__(self, item):
		node=self._head
		while node != None:
			if node.value == item:
				return True
				node=node.link
			else:
				return False

	def __iter__(self):
		return LinkedListIter(self)

	def __len__(self):
		return self._nodeCount

LL = LinkedList()
LL.addFirst(10)
LL.addLast(20)
LL.addAt(0,[])
LL.addAt(2,[1,2,3])
print(str(LL)) #"[[];10;[1, 2, 3];20]")
