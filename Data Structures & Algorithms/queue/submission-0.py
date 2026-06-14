class Deque:
    from collections import deque
    
    def __init__(self):
        self.queue = collections.deque()

    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False
        

    def append(self, value: int) -> None:
        self.queue.append(value)

    def appendleft(self, value: int) -> None:
        self.queue.appendleft(value)

    def pop(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue.pop()

    def popleft(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue.popleft()
        
