class LinkedListIter:
  def __init__(self, lst):
    self.lst=lst
    self.it=iter(lst.L)

  def __next__(self):
    return next(self.it)

  def __iter__(self):
      return self

class LinkedList:
  def __init__(self, lst=[], size=0):
    self.L=lst
    self.size=size

  def addLast(self, x):
      self.L.append(x)
      self.size+=1

  def addFirst(self, x):
    self.L=[x]+self.L
    self.size+=1

  def removeFirst(self):
      if self.L==[]:
          return None
      else:
          self.L.pop(0)
          self.size-=1

  def removeLast(self):
      if self.L==[]:
         return None
      else:
          self.L.pop()
          self.size-=1

  def addAt(self, idx, x):
      sum=0
      for i in self.L:
          sum+=1
      if sum < idx:
          return False
      else:
        self.L = self.L[:idx] + [x] + self.L[idx:]
        self.size+=1
        return True
        return self.L


  def removeAt(self, idx):
      sum=0
      for i in self.L:
          sum+=1
      if sum < idx:
          return False
      else:
        self.L.pop(idx)
        self.size-=1
        return True
        return self.L


  def __str__(self):
    str=""
    for x in self.L:
        str = str + "%s" % (x) +";"
    return "[" + str[0:-1] + "]"

  def __contains__ (self, x):
    for i in self.L:
        if i==x:
            return True
        else:
            return False
  def __setitem__(self, idx, x):
      sum=0
      for i in self.L:
          sum+=1
      if idx < sum :
          self.L[idx] = x
      else:
          raise Exception("Invalid index" + "%" % idx)

  def __getitem__(self, idx):
    if idx < self.size :
        return self.L[idx]
    else:
        raise Exception("Invalid index" + "%" % idx)

  def __iter__(self):
    return LinkedListIter(self)

  def __len__(self):
    return self.size
