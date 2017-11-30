import stdio

class Queue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
    
    def enqueue(self, item):
        return self.in_stack.append(item)
    
    def dequeue(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack.pop()
        else:
            return 'queue empty'
    
    def peek(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack[-1]
        else:
            return 'queue empty'

    def size(self):
        return len(self.in_stack) + len(self.out_stack)
    
    def isEmpty(self):
        return not ( bool(self.in_stack) or bool(self.out_stack) )

    def __str__(self):
        _string_ = ''
        if not self.out_stack: #este algoritmo para representar um queue pode ser melhorado,
            self._transfer() #pois se haver uma segunda onda de inserções (for in range) ele só irá representar o primeiro list out_stack até que este fique vazio
        if self.out_stack:
            return 'tail {} head'.format(self.out_stack)
        else:
            return 'queue empty'

if __name__ == "__main__":
    q = Queue()
    stdio.writeln("Is the queue empty? {}".format(q.isEmpty() ))
    for i in range(10,30, 3):
        q.enqueue(i)
    stdio.writeln(q)
    stdio.writeln("Is the queue empty? {}".format(q.isEmpty() ))
    stdio.writeln("Queue size? {}".format(q.size() ))
    stdio.writeln("Queue peek? {}".format(q.peek() ))
    stdio.writeln("Queue dequeue? {}".format(q.dequeue() ))
    stdio.writeln("Queue peek? {}".format(q.peek() ))
    for i in range(30,90, 3):
        q.enqueue(i)
    stdio.writeln(q)
    stdio.writeln("Queue size? {}".format(q.size() ))
    stdio.writeln("Queue peek? {}".format(q.peek() ))
    stdio.writeln("Queue dequeue? {}".format(q.dequeue() ))
    stdio.writeln("Queue peek? {}".format(q.peek() ))
