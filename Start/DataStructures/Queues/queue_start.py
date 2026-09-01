# Example file for Programming Foundations: Algorithms by Joe Marini
# try out the Python queue functions
from collections import deque

# TODO: create a new empty deque object that will function as a queue
de = []

#use deque as an object
queue = deque()

# TODO: add some items to the queue
de.append(1)
de.append(2)
de.append(3)
de.append(4)

queue.append(5)
queue.append(6)
queue.append(7)
queue.append(8)

# TODO: print the queue contents
print(de)
print(queue)

# TODO: pop an item off the front of the queue
x = de.pop(0)
print(x)
print(de)

y = queue.popleft()
print(y)
print(queue)