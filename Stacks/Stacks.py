# there are two ways to implement stacks

# using array
# using linked list


#implement using array method
from sys import maxsize


def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print(item+'pushed to stack')


def pop(stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack.pop()


def peek(stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack[len(stack)-1]


if __name__ == '__main__':
    stack = createStack()
    push(stack, str(10))
    push(stack, str(20))
    push(stack, str(30))
    print(peek(stack),'is peek')
    print(pop(stack),'pop from stack')


#implement using linked list method

class StackNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False
    
    def push(self,data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        print('push stack ',data)


    def pop(self):
        if self.isEmpty():
            return float('-inf')
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped
    
    def peek(self):
        if self.isEmpty():
            return float('-inf')
        return self.root.data

if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print('popped from stack',stack.pop())
    print('top element is ',stack.peek())
