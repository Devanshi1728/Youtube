import queue

q=queue.PriorityQueue()

q.put((5,'Ahmedabad'))
q.put((2,'Baroda'))
q.put((3,'Canada'))
q.put((1,'Delhi'))

for i in range(q.qsize()):
    print(q.get()[1])

'''
Delhi
Baroda
Canada
Ahmedabad
'''

qu=queue.LifoQueue()

for i in range(1,5) :
    qu.put(i**2);

while not qu.empty():
    print(qu.get(),end=" ")


'''
16 9 4 1 
'''
