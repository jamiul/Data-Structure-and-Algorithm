class Stack:
    def __init__(self):
        self.ara = []
  # Use list append method to push
    def add(self,data):
        if data not in self.ara:
            self.ara.append(data)
            return True
        else:
            return False
    # Use list pop method to remove
    def remove(self):
        if len(self.ara) <= 0:
            return("Empty Stack")
        else:
            return self.ara.pop()

    # Peek 1st Element of the Stack
    def peek(self):
        return self.ara[0]

   # Show Stack
    def show(self):
        print("Push Elements: ")
        for x in self.ara:
            print(x)


s = Stack()
s.add("Sun")
s.add("Mon")
s.show()
print("Peek 1st Element: ")
s.peek()
print(s.peek())
print("Pop Element: ")
s.remove()
print(s.remove())
