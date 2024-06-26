
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
        
        

exp1 = 'a-b+t/6'
infix = list(exp1)

# creating stack instance
stack1 = Stack(len(infix))

def precedence(char):
    if char == '*' or char == '/':
        return 3
    elif char == '+' or char == '-':
        return 2
    else:
        return 0
    
def isOperator(char):
    if char == '+' or char == '-' or char == '/' or char == '*':
        return True
    return False

def infixToPostfix(infix):
    postfix = [None]*len(infix)

    i = 0 # pointer for infix
    j = 0 # pointer for postfix addition

    while(i<len(infix)):

        if(not isOperator(infix[i])):
            postfix[j] = infix[i]
            i += 1
            j += 1
        else:
            # Gonna check whether its prec is higher than the top of stack
            if (precedence(infix[i]) > precedence(stack1.arr[stack1.top])):
                stack1.push(infix[i])
                i += 1
            else:
                element = stack1.pop()
                postfix[j] = element
                j += 1
    # Another while loop to pop everything and add to the postfix
    while (not stack1.isEmpty()):
        element = stack1.pop()
        postfix[j] = element
        j += 1
    
    return postfix

output = infixToPostfix(infix)
print('The Infix is - ', infix)
print('The Postfix is - ', output)
                
