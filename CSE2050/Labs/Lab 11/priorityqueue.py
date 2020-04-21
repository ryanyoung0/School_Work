import time
import random
import os
#==============  TreeNode class  =================

class TreeNode:
  def __init__(self, val, parent=None):
    self.height = 1
    self.val = val
    self.parent = parent
    self.leftChild = None
    self.rightChild = None
    self.height1 = 1

  def hasLeftChild(self):
    return self.leftChild

  def hasRightChild(self):
    return self.rightChild

#==============  PQ class  =================

class PQ:
  def add(self,val):
    raise NotImplemented

  def peekMin(self):
    raise NotImplemented

  def getMin(self):
    raise NotImplemented

  def __len__(self):
    raise NotImplemented

# ============== LIST CLASS ==================

class ListPQ(PQ):
  def __init__(self):
    self.items = []

  def __len__(self):
    return len(self.items)

  def add(self, val):
    self.items.append(val)

  def peekMin(self):
    return self.getMin(False)

  def getMin(self, toRemove=True):
    if (self.items == []):
      return None
    minIdx = 0
    sz = len(self.items)
    for idx in range(sz):
      if priority(self.items[idx]) < priority(self.items[minIdx]):
        minIdx = idx
    minItem = self.items[minIdx]
    if toRemove:
      del self.items[minIdx]
    return minItem

  def draw(self):
    print(self.items)

# ============== BST CLASS ==================

class BST(PQ):

  def __init__(self):
    self.root = None
    self.size = 0

  def __len__(self):
    return self.size

  ## Part 2
  def add(self, val):
      print ("calling add for BST, value", val)
      if self.root == None:
          nN = TreeNode(val)
          self.root = nN
      else:
          cn = self.root
          while cn != None:
              if priority(val) < priority(cn.val):
                  if cn.leftChild is None:
                      nN = TreeNode(val, cn)
                      cn.leftChild = nN
                      break
                  else:
                      cn = cn.leftChild
              else:
                  if cn.rightChild is None:
                      nN = TreeNode(val, cn)
                      cn.rightChild = nN
                      break
                  else:
                      cn = cn.rightChild
      self.size += 1
      return nN


    ## need to implement setting parents and need to

  def peekMin(self):
    return self.getMin(False)

  def getMin(self, toRemove=True):
    cn = self.root
    if not cn:
      return None
    while cn.leftChild != None:
      cn = cn.leftChild
    if toRemove:
      self._remove(cn)   ## TO IMPLEMENT
      self.size -= 1
    return cn.val

  ## Part 3
  def _remove(self, node):
      print("***********before removing ", node.val)
      cn = node
      if cn.parent == None:
          self.root = None
      elif cn.rightChild != None:
          cn.parent.leftChild = cn.rightChild
          cn.parent.leftChild.leftChild = cn.leftChild
      elif cn.leftChild != None:
          cn.parent.leftChild = cn.leftChild
      else:
          cn.parent.leftChild = None
      self.draw()

  def draw(self):
    drawTree(self.root, 0, True)

# ================ class BalancedBST ===============

class BalancedBST(BST):

    def height_updater(self, node):
        if node == None:
            return 0
        node.height = 1 + max(self.height_updater(node.leftChild),self.height_updater(node.rightChild))
        node.height1 = node.height
        return node.height

    def add(self,val):
      newNode = BST.add(self, val)
      while newNode is not None:
          self.height_updater(newNode)
          if newNode.leftChild is not None or newNode.rightChild is not None:
              if newNode.leftChild is None:
                  bf = 0 - newNode.rightChild.height
              elif newNode.rightChild is None:
                  bf = newNode.leftChild.height - 0
              else:
                  bf = newNode.leftChild.height - newNode.rightChild.height
              if bf > 1 or bf < -1:
                  if bf < 0:
                      if newNode.rightChild.leftChild is None:
                          bf_right = 0 - newNode.rightChild.rightChild.height
                      elif newNode.rightChild.rightChild is None:
                          bf_right = newNode.rightChild.leftChild.height - 0
                      else:
                          bf_right = newNode.rightChild.leftChild.height - newNode.rightChild.rightChild.height
                      if bf_right > 0:
                          self.rotateRight(newNode.rightChild)
                          self.height_updater(newNode)
                          self.rotateLeft(newNode)
                          self.height_updater(newNode)
                      else:
                          self.rotateLeft(newNode)
                          self.height_updater(newNode)
                  else:
                      if newNode.leftChild.leftChild is None:
                          bf_left = 0 - newNode.leftChild.rightChild.height
                      elif newNode.leftChild.rightChild is None:
                          bf_left = newNode.leftChild.leftChild.height - 0
                      else:
                          bf_left = newNode.leftChild.leftChild.height - newNode.leftChild.rightChild.height
                      if bf_left < 0:
                          self.rotateLeft(newNode.leftChild)
                          self.height_updater(newNode)
                          self.rotateRight(newNode)
                          self.height_updater(newNode)
                      else:
                          self.rotateRight(newNode)
                          self.height_updater(newNode)
          newNode = newNode.parent
      return newNode

    def rotateLeft(self, rotRoot):
        nr = rotRoot.rightChild
        rotRoot.rightChild = nr.leftChild
        if nr.leftChild != None:
            nr.leftChild.parent = rotRoot
        nr.parent = rotRoot.parent
        if rotRoot == self.root:
            self.root = nr
        else:
            if rotRoot.hasLeftChild:
                rotRoot.parent.leftChild = nr
            else:
                rotRoot.parent.rightChild = nr
        nr.leftChild = rotRoot
        rotRoot.parent = nr

    def rotateRight(self, rotRoot):
        nr = rotRoot.leftChild
        rotRoot.leftChild = nr.rightChild
        if nr.rightChild != None:
            nr.rightChild.parent = rotRoot
            nr.parent = rotRoot.parent
        if rotRoot == self.root:
            self.root = nr
        else:
            if rotRoot.hasRightChild:
                rotRoot.parent.rightChild = nr
            else:
                rotRoot.parent.leftChild = nr
        nr.rightChild = rotRoot
        rotRoot.parent = nr

    def draw(self):
        drawTree(self.root, 0, True)

# ============== simulator ======================

class Simulator:

  def __init__ (self, newPQ, isLoud=True):
    self.pq = newPQ
    self.limit = -1
    self.clock = 0
    self.log = None
    self.addTime = 0
    self.getTime = 0
    self.isLoud = isLoud

  def setLimit(self, num):
    self.limit = num

  def useLog(self, log):
    self.log = log

  def _getNextEvent(self):
    self.clock += 1  # timestamps start at 1 and go up
    if self.log:
      idx = self.clock - 1
      if idx >= len(self.log):
        return None
      line = self.log[self.clock -1 ]
      #print ("found line", line)
      if line[0] == 'g':
        return ()
      else:
        nums = line[2:-1].split(',')
        return (int(nums[0]), int(nums[1]))
    else:  # either generate a new task or get existing task to process
      num = random.randint(1,22)
      isNew = (num % 7 < 4)  # 4/7 of the time we have new task
      if isNew:
        return (num, self.clock)
      else:
        return ()

  def run(self):
    if self.isLoud:
        print("Simulation starting, PQ is ", type(self.pq), ", using log:", bool(self.log), ", limit is", self.limit)
    log = []
    while (self.limit == -1 or self.clock < self.limit):
      val = self._getNextEvent()
      if val == None:
        break
      elif len(val) > 0: # a new task has been generated for processing
        if self.isLoud:
          print("New task", val, "has been generated")
        startTime = time.time()
        self.pq.add(val)
        endTime = time.time()
        log.append("n" + str(val))
        self.addTime += endTime - startTime
      else:
        startTime = time.time()
        val = self.pq.getMin() # system is ready to process next task
        endTime = time.time()
        if self.isLoud:
          print(val, "is being processed next")
        log.append("g" + str(val))
        self.getTime += endTime - startTime
    if self.isLoud:
      self.pq.draw()
    print("Simulation finished,", type(self.pq), "has size", len(self.pq))
    return log

# ============== additional methods ==================

## Part 1
def priority(val):
    return val

def drawTree(node, indent=0, showHeight=False):
  if node == None:
    return
  drawTree(node.rightChild, indent+1, showHeight)
  if node.rightChild:
    print("     " * indent, "  / ")
  if showHeight:
    print("     " * indent, node.val, ", height", node.height1)
  else:
    print("     " * indent, node.val)
  if node.leftChild:
    print("     " * indent, "  \ ")
  drawTree(node.leftChild, indent+1, showHeight)

# =================  testing around ===================

#x = ListPQ() # we can also do BST or BalancedBST here
#x.add(5)
#x.add(9)
#x.add(11)
#x.add(10)
#x.add(3)
#x.add(4)
#x.draw()
#len(x) #should be 6, highest priority is 3
#print("This", type(x), "has", len(x), "items, highest priority is", x.peekMin())
#y = x.getMin()
#print("Removed", y, "here is what's left")
#x.draw()

#s1 = Simulator(BalancedBST()) # interactive simulator with BalancedBST impl
#s1.setLimit(17) # will stop after processing 17 events
#s1.run()

#s = Simulator(ListPQ(),False) # this will be a long run, don't want it loud
#s.setLimit(10000) # will stop after processing 10000 events
#log = s.run()

#s2 = Simulator(ListPQ(), False)
#s2.useLog(log) # this will run from log
#log1 = s2.run()  # log and log1 should be identical
#rint("Total add time:", s2.addTime, "; Total get time:", s2.getTime)

#s3 = Simulator(BST(), False)
#s3.useLog(log) # this will run from log
#log1 = s3.run()  # log and log1 should be identical
#print("Total add time:", s3.addTime, "; Total get time:", s3.getTime)

#once balancing is implemented, we want to compare the times of various impls for long runs!!
