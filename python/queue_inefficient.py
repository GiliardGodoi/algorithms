
class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)
    
    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
    
    def __repr__(self):
        return '{}'.format(self.items)
    
    def __str__(self):
        return '{}'.format(self.items)

if __name__ == "__main__":
    q = Queue()
    stdio.writeln("Is the queue empty? {}".format(q.isEmpty() ))
    for i in range(10,30):
        q.enqueue(i)
    stdio.writeln(q)
    stdio.writeln("Is the queue empty? {}".format(q.isEmpty() ))
    stdio.writeln("Queue size? {}".format(q.size() ))
    stdio.writeln("Queue peek? {}".format(q.peek() ))
    stdio.writeln("Queue dequeue? {}".format(q.dequeue() ))
    stdio.writeln("Queue peek? {}".format(q.peek() ))
