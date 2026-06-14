class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next = nxt

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        dummyNode = self.head
        curr = dummyNode.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr == None or index > 0:
            return -1
        return curr.val


    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        curr = self.head.next
        newNode.next = curr
        if newNode.next == None:
            self.tail = newNode
        self.head.next = newNode
        
    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        while curr and index:
            curr = curr.next
            index -= 1

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
                


    def getValues(self) -> List[int]:
        ret = []
        curr = self.head.next
        while curr:
            ret.append(curr.val)
            curr=curr.next
        return ret

        
