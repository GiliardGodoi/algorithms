from linked_list_fifo import LinkedListFIFO
import stdio

class HashTable(object):
    def __init__(self, slots=10):
        self.slots = slots
        self.table = []
        self.create_table()
    
    def hash_key(self,value):
        return hash(value) % self.slots
    
    def create_table(self):
        for i in range(self.slots):
            self.table.append([])
    
    def add_item(self, value):
        key = self.hash_key(value)
        self.table[key].append(value)
    
    def print_table(self):
        for j in range(len(self.table)):
            stdio.writeln("Key %s, value is %s" % (j,self.table[j]) )
    
    def find_item(self, item):
        pos = self.hash_key(item)
        return (item in self.table[pos])

if __name__ == "__main__":
    h = HashTable(5)
    for i in range(1,40,2):
        h.add_item(i)
    h.print_table()
    assert(h.find_item(20) == False)
    assert(h.find_item(21) == True)