import heapq
import stdio

h = []
heapq.heappush(h,(1,'food'))
heapq.heappush(h, (2, 'have fun') )
heapq.heappush(h, (3 , 'work') )
heapq.heappush(h, (4, 'study') )

stdio.writeln(h)
stdio.writeln(heapq.heappop(h))
stdio.writeln(h)