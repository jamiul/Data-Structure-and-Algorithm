# Create Node
# Create Linkedlist
# Add nodes to Linkedlist
# Print Linkedlist
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.root = None

    def InsertNode(self,newNode):
        if self.root is None:
            self.root = newNode
        else:
            lastNode = self.root
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def PrintList(self):
        currentNode = self.root
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


nodeOne = Node("Jamiul")
listOne = Linkedlist()
listOne.InsertNode(nodeOne)
nodeTwo = Node("Jahir")
listOne.InsertNode(nodeTwo)
nodeThree = Node("Rifat")
listOne.InsertNode(nodeThree)
listOne.PrintList()
