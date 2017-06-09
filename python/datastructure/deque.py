from collections import deque
import stdio

q = deque(['blue', 'yellow', 'red'])
stdio.writeln(q)
q.append('green')
stdio.writeln(q)
stdio.writeln(q.popleft())
stdio.writeln(q.pop())
stdio.writeln(q)

stdio.writeln(q.appendleft('purple'))
stdio.writeln(q)