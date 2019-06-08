
class Node():
    def __init__(self, value = None, pointer = None):
        self.value = value
        self.pointer = pointer

    def setNext(self,node):
        self.pointer = node
    
    def getNext(self):
        return self.pointer
    
    def setData(self, new_value):
        self.value = new_value
    
    def getData(self):
        return self.value