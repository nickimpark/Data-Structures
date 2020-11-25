class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return (self.items == [])

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# Last in, first out

"""
myStack = Stack()
s = input().split()
for i in s:
    myStack.push(i)
while not myStack.isEmpty():
    print(myStack.pop())
"""
