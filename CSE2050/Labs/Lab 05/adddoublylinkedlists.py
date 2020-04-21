class ListNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next
        if prev is not None:
            self.prev.next = self
        if next is not None:
            self.next.prev = self

class DoublyLinkedList:
    def __init__(self, string = ''):
        self.head=None
        self.tail=None
        self._length=(len(string))
        self.isReversed = False
        for x in string:
            self.addLast(int(x))

    def addFirst(self, item):
        self._length +=1
        node=ListNode(item, next = self.head)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            self.head = node

    def addLast(self, item):
        self._length += 1
        if self.head == None:
            self.addFirst(item)
        else:
            self.tail = ListNode(item, self.tail, None)


    def reverse(self):
        if self.isReversed == True:
            head1 = self.head
            for x in range(self._length):
                nxt = head1.next
                prev = head1.prev
                head1.next = prev
                head1.prev = nxt
            head2 = self.head
            self.head = self.tail
            self.tail = head2
        else:
            head1 = self.head
            for x in range(self._length):
                nxt = head1.next
                prev = head1.prev
                head1.prev = nxt
                head1.next = prev
            head2 = self.head
            self.head = self.tail
            self.tail = head2
            self.isReversed = True

    def fastReverse(self):
        self.isReversed = True
        head = self.head
        tail = self.tail
        self.head = tail
        self.tail = head

    def __str__(self):
        strng = ""
        head=self.head
        while head != None:
            strng += (str(head.value))
            head = head.next
        return (strng.strip("0"))

    def __len__(self):
        return self._length

def sumlinkednumbers(dll1, dll2):
    cur1 = dll1.tail
    cur2 = dll2.tail
    carry = 0
    TEDLL= DoublyLinkedList()
    while cur1 != None or cur2 != None:
        if cur1 == None:
            n = 0
            n2 =  int(cur2.value)
        elif cur2 == None:
            n2 = 0
            n = int(cur1.value)
        else:
            n = int(cur1.value)
            n2 = int(cur2.value)
        sum = n + n2 + carry
        num = sum % 10
        carry = sum // 10
        TEDLL.addFirst(num)
        try:
            if dll2.isReversed == True:
                cur2 = cur2.next
            else:
                cur2 = cur2.prev
        except AttributeError:
            cur2 = None
        try:
            if dll1.isReversed == True:
                cur1 = cur1.next
            else:
                cur1 = cur1.prev
        except AttributeError:
            cur1 = None
    return TEDLL
