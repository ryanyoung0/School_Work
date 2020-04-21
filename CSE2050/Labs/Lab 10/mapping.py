import operator
import time
import math

class Entry:
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def __str__(self):
		return "%d: %s" % (self.key, self.value)


class ListMapping:
	def __init__(self):
		self._entries = []

	def put(self, key, value):
		e = self._entry(key)
		if e is not None:
			e.value = value
		else:
			self._entries.append(Entry(key, value))

	def get(self, key):
		e = self._entry(key)
		if e is not None:
			return e.value
		else:
			raise KeyError

	def _entry(self, key):
		for e in self._entries:
			if e.key == key:
				return e
		return None

	def _entryiter(self):
		return (e for e in self._entries)

	def __str__(self):
		return str([str(e) for e in self._entries])

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, value):
		self.put(key, value)

	def __len__(self):
		return len(self._entries)

	def __contains__(self, key):
		if self._entry(key) is None:
			return False
		else:
			return True

	def __iter__(self):
		return (e.key for e in self._entries)

	def values(self):
		return (e.value for e in self._entries)

	def items(self):
		return((e.key, e.value) for e in self._entries)


## Part 2
class HashMapping:
	def __init__(self, size = 1000):
		self._size = size
		self._buckets = [ListMapping() for e in range(self._size)]
		self._length = 0

	def __iter__(self):
		return (e.key for e in self._entryiter())

	def _entryiter(self):
		return (e for buck in self._buckets for e in buck._entryiter())

	def values(self):
		return (e.value for e in self._entries)

	def _bucket(self, key):
		return self._buckets[hash(key) % self._size]

	def items(self):
		return ((e.key, e.value) for e in self._entryiter())

	def get(self, key):
		buck = self._bucket(key)
		return buck[key]

	def __getitem__(self, key):
		return self.get(key)

	def put(self, key, value):
		buck = self._bucket(key)
		if key not in buck:
			self._length += 1
		buck[key] = value

	def __setitem__(self, key, value):
		self.put(key, value)

	def __contains__(self, key):
		try:
			self.get(key)
		except KeyError:
			return False
		return True

	def __len__(self):
		return self._length

	def statistics(self):
		totall = self._size
		a = 0
		for i in self._buckets:
			if i._entries == []:
				a += 1
		empty = a
		lst = [len(i._entries) for i in self._buckets]
		largest = max(lst)
		total = 0
		for i in lst:
			total += i
		average = total / (totall - empty)
		dv = 0
		for i in self._buckets:
			f = len(i._entries) - average
			fsqr = f * f
			dv += fsqr
		avgdv = dv / totall
		sdv = math.sqrt(avgdv)
		print("Total number of buckets: ", totall)
		print("Number of empty buckets: ", empty)
		print("Size of the largest buckets: ", largest)
		print("Average size: ", avgdv)
		return (totall, empty, largest, average, avgdv)

## Part 3
class ShakespeareToken(str):
	def __init__(self, string):
		self._string = string
		self._length = len(string)

	def __hash__(self):
		return self._length

## Part 4
class ShakespeareToken2(str):
	def __init__(self, string):
		self._string = string
		self._length = len(string)

	def __hash__(self):
		accm = 0
		for e in self._string:
			accm += int(ord(e))
		return accm

class ShakespeareToken3(str):
	def __init__(self, string):
		self._string = string
		self._length = len(string)

	def __hash__(self):
		hv = 0
		for e in range(len(self)):
			hv += ord(self[e]) * (53 ** e)
		return hv


class ExtendableHashMapping(HashMapping):
	def get(self, key):
		buck = self._bucket(key)
		return buck[key]

	def put(self, key, value):
		buck = self._bucket(key)
		if key not in buck:
			self._length += 1
		buck[key] = value
		if self._length > self._size:
			self._double()

	def getitem(self, key):
		return self.get(key)

	def setitem(self, key, value):
		self.put(key, value)

	def _double(self):
		old = self._buckets
		self._size *= 2
		self._buckets = [ListMapping() for x in range(self._size)]
		for i in old:
			for key, value in i.items():
				k = self._bucket(key)
				k[key] = value



## Part 1
def getTokensFreq(file):
	f = open(file, "r")
	data = f.read()
	f.close()
	data = data.split()
	d = {}
	lower = [e.lower() for e in data]
	for i in lower:
		if i in d.keys():
			d[i] += 1
		else:
			d[i] = 1
	return d

def getMostFrequent(d, k):
	tl = []
	accm = 0
	lst = sorted(d)
	if accm == k:
		return tl
	else:
		tl.append(l[accm])
		accm += 1
