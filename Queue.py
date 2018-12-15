# In Queue follow FIFO (First in First Out)
class Queue:
    def __init__(self):
        self.queue = list()
    # Enqueue data into a Queue
    def add(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        else:
            return False

   # Dequeue data from Queue
    def remove(self):
        if len(self.queue) <= 0:
            print("Empty Queue")
        else:
            return self.queue.pop()

    # Display Queue List
    def display(self):
        print(self.queue)
        #for i in range(len(self.queue)):
        #    print(self.queue[i],end=' ')

myQueue = Queue()
myQueue.add("Mango")
myQueue.add("Apple")
myQueue.add("Orange")
myQueue.display()
print(myQueue.remove())
