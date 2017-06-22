import heapq

class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "Item({!r})".format(self.name)
def test():
    q = PriorityQueue()
    q.push(Item('item 1'), 1)
    q.push(Item('item 2'), 4)
    q.push(Item('item 3'), 7)
    q.push(Item('item 4'), 3)
    assert(str(q.pop()) == "Item('item 3')")


test()