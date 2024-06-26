
# In Parenthesis Matching we check whether the given expression containing parenthesis is balanced or not 

"""
The Conditions for a balanced parenthesis expression are -

1) While popping element from the stack, The stack should not underflow. If happens then that means it is an unbalanced expression

2) At the end of the expression the stack must be empty.

"""

# Here we are creating a class for stack


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


# The given expression in terms of a list/array

exp1 = '3*2-(8+1)'
exp1 = list(exp1)

exp2 = '[7-(8+2)-}7*4]'
exp2 = list(exp2)

exp3 = '[7-(8+2)-{7*4}]'
exp3 = list(exp3)

# creating stack instance
stack1 = Stack(len(exp1))   # size should be equal to the length of the expression
stack2 = Stack(len(exp2))   # size should be equal to the length of the expression
stack3 = Stack(len(exp3))   # size should be equal to the length of the expression


# First we are gonna run a loop from the start to end of the array

def isMatching(a,b):
    if a == '(' and b == ')':
        return True
    if a == '{' and b == '}':
        return True
    if a == '[' and b == ']':
        return True
    return False

def expStatus(exp1,stack):

    count = 0
    for i in exp1:
        if i == '(' or i == '{' or  i == '[':
            stack.push(i)
            count += 1
        if i == ')' or i == '}' or i == ']':
            count += 1
            if stack.isEmpty():
                return f"The Expression is Unbalanced , Steps Taken - {count}"
            popped_value = stack.pop()
            if not isMatching(popped_value,i):
                return f"The Expression is Unbalanced, Steps Taken - {count}"

    if stack.isEmpty():
        return f'The Expression is Balanced, Steps Taken - {count}'
    else:
        return f'The Expression is Unbalanced , Steps Taken - {count}'
    

# Checking whether the exp is balanced of not 

status = expStatus(exp1, stack1)
print(status)

status = expStatus(exp2,stack2)
print(status)

status = expStatus(exp3,stack3)
print(status)

