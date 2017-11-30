import stdio

class Node(object):
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer

class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0
        self.iter_pointer = None
    
    def isEmpty(self):
        return not bool(self.head)
    
    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            return value
        else:
            return 'queue is empty'
    
    def enqueue(self,value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        elif self.tail:
            self.tail.pointer = node
            self.tail = node
        self._length += 1
    
    def size(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.pointer
        return count
    
    def peek(self):
        if self.head:
            return self.head.value
    
    def __len__(self):
        return self._length
        
    def __str__(self):
        _string_ = ''
        node = self.head
        while node:
            _string_ += (str(node.value) + '-> ' )
            node = node.pointer
        return _string_
    
    def __iter__(self):
        self.iter_pointer = self.head
        return self
    
    def next(self):
        if self.iter_pointer :
            value = self.iter_pointer.value
            self.iter_pointer = self.iter_pointer.pointer
            return value
        else :
            raise StopIteration()

    
    def _print(self):
        node = self.head
        while node:
            stdio.writeln(node.value)
            node = node.pointer

if __name__ == "__main__":
    q = LinkedQueue()
    stdio.writeln("Is the queue empty? {}".format(q.isEmpty() ))
    for i in range(10,30, 3):
        q.enqueue(i)
    stdio.writeln(q)
    stdio.writeln("Is the queue empty? {}".format(q.isEmpty() ))
    stdio.writeln("Queue size? {}".format(q.size() ))
    stdio.writeln("Queue peek? {}".format(q.peek() ))
    stdio.writeln("Queue dequeue? {}".format(q.dequeue() ))
    stdio.writeln("Queue peek? {}".format(q.peek() ))