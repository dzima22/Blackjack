class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length==0:
            return None
        temp=self.first
        if self.length==1:
            self.first=None
            self.last=None
        else:
            self.first=temp.next
            temp.next=None
        self.length-=1
        return temp
            
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height==0:
            return None
        else:
            temp=self.top
            self.top=temp.next
            temp.next=None
            self.height-=1
            return temp
            
class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if len(self.stack_list)==0:
            return None
        else:
            temp=self.stack_list[-1]
            self.stack_list.pop()
            return temp
    def reverse_string(string):
        stack=Stack()
        reverse_string=""
        for i in string:
            stack.push(i)
        while not stack.is_empty():
            reverse_string+=stack.pop()
        return reverse_string
def is_balanced_parentheses(string):
    if len(string)==0:
        return True
    stack=Stack()
    for i in string:
        if i=="(":
            stack.push(i)
        if i==")":
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
def sort_stack(stack):
    stack2=Stack()
    while not stack.is_empty():
        temp=stack.pop()
        while not stack2.is_empty() and temp<stack2.peek():
            stack.push(stack2.pop())
        stack2.push(temp)
    while not stack2.is_empty():
            stack.push(stack2.pop())
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self,number):
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())
            self.stack1.append(number)
            while len(self.stack2)!=0:
                self.stack1.append(self.stack2.pop())
            

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
    def enqueue(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if len(self.stack1)==0:
            return None
        else:
            temp=self.stack1.pop()
        return temp 

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0