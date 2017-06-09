
class Stack(object):

    def __init__(self):
        self.content = []
        self.min_array = []
        self.min = float('inf')
    
    def __repr__(self):
        return '{}'.format(self.content)
    
    def push(self, value):
        if value < self.min:
            self.min = value
        self.content.append(value)
        self.min_array.append(self.min)
    
    def pop(self):
        if self.content:
            value = self.content.pop()
            self.min_array.pop()
            if self.min_array:
                self.min = self.min_array[-1]
            return value
        else:
            return 'Empty list'
    
    def find_min(self):
        if self.min_array:
            return self.min_array[-1]
        else:
            return 'No min value for empty list'
    
    def top(self):
        if self.content:
            return self.content[-1]
        else:
            return 'stack is empty'
    
    def size(self):
        return len(self.content)
    
    def isEmpty(self):
        return not bool(self.content)
if __name__ == '__main__':
    pilha = Stack()
    for i in range(15,20):
        pilha.push(i)
    for i in range(10,5,-1):
        pilha.push(i)
    for i in range(1,13):
        print pilha.pop(), pilha.find_min()