
# Stack using array , The time complexity of push pop peek stacktop stackbottom isFull isEmpty is - O(1)

class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.arr = [None] * size

    def isEmpty(self):
        if self.top == -1:
            return 1
        return 0

    def isFull(self):
        if self.top == self.size - 1:
            return 1
        return 0
    
    def push(self,value):
        if(self.isFull()):
            print('Stack Overflow')
        else:
            self.top += 1
            self.arr[self.top] = value
        
    def pop(self):
        if self.isEmpty():
            print('The Stack is Empty')
            return -1
        else:
            popped_value = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return popped_value
        
    def peek(self,position):
        if (self.top - position + 1) < 0:
            return "Invalid Position"
        else:
            return self.arr[self.top - position + 1]

# creating stack instance
stack = Stack(8)


# print('The Stack - ', stack.arr)
stack.push(10)
stack.push(11)
stack.push(198)
stack.push(99)

# printing the values from the stack
for j in range(stack.top + 1):
    j += 1
    print(f'The element at position {j} is - {stack.peek(j)}')

# print("Peek the first element from top basically position -  ", stack.peek(2))

# print(stack.pop())

# print(f'The Stack with top - {stack.top} - ', stack.arr)
# print(stack.arr[stack.top])

# Manually adding an element into the stack
# stack.arr[0] = 10
# stack.top += 1

# if stack.isEmpty():
#     print('The stack is empty')
# else:
#     print('The stack is not empty')
