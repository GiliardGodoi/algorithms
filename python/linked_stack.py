import stdio

class Node(object):
    def __init__(self,value=None, pointer = None):
        self.value = value
        self.pointer = pointer
        self.size = 0

class Stack(object):

    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self): 
        return not bool(self.head)
    
    def push(self, item):
        self.head = Node(item,self.head)
        self.size += 1
    
    def pop(self):
        if self.head:
            node = self.head
            self.head = node.pointer
            self.size -= 1
            return node.value
        else :
            return 'stack is empty'
    
    def top(self):
        if self.head :
            return self.head.value
        else :
            return 'stack is empty'
    
    def get_size(self):
        return self.size
    
    def count(self):
        node = self.head
        count = 0
        while node :
            count += 1
            node = node.pointer
        return count
    
    def _printStack(self):
        node = self.head
        while node :
            print node.value
            node = node.pointer

if __name__ == "__main__":
    stack = Stack()
    stdio.writeln("Is the stack empty? {}".format(stack.isEmpty()) )
    for i in range(10):
        stack.push(i)
    stack._printStack()
    stdio.writeln("Stack size: {}".format(stack.get_size() ))
    stdio.writeln("Stack count: {}".format(stack.count() ))
    stdio.writeln("pop... {}".format(stack.pop() ))
    stdio.writeln("peek ... {}".format(stack.top()  ))
    stdio.writeln("Is the stack empty? {}".format(stack.isEmpty()) )


