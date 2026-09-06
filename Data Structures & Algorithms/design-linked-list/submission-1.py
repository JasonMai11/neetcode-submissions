class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.size = 0
        

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        if curr: 
            return curr.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

        if self.size == 0:
            self.tail = node
        self.size += 1

        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        self.tail.next = node
        self.tail = node
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        node = Node(val)
        node.next = prev.next
        prev.next = node

        if index == self.size:
            self.tail = node
        
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        removed = prev.next
        prev.next = removed.next

        if removed is self.tail: self.tail = prev
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)