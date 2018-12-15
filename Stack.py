# LIFO (Last in First out)
class Stack:
    def __init__(self):
        self.stack = [ ]

    def add(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def remove(self):
        if len(self.stack) <= 0:
            print("Empty Stack")
        else:
            return self.stack.pop()

    def display(self):
        for i in range(len(self.stack)):
            print(self.stack[i])

myStack = Stack()
myStack.add("Mango")
myStack.add("Apple")
myStack.add("Orange")
myStack.display()
print(myStack.remove())
