#Back-end complete function Template for Python 3
# Python program to convert infix expression to postfix

# Class to convert the expression
class Evaluate:

    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []

        # check if the stack is empty

    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

        # Pop the element from the stack

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)

        # The main function that converts given infix expression

    # to postfix expression
    def evaluatePostfix(self, exp):

        # Iterate over the expression for conversion
        for i in exp:

            # If the scanned character is an operand
            # (number here) push it to the stack
            if i.isdigit():
                self.push(i)

                # If the scanned character is an operator,
            # pop two elements from stack and apply it.
            else:
                val1 = self.pop()
                val2 = self.pop()
                if(i=='/'):
                    p="//"
                    self.push(str(eval(val2 + p + val1)))
                else:
                    self.push(str(eval(val2 + i + val1)))

        return (self.pop())
'''
Function Arguments :
		@param  : S (given postfix expression)
		@return : Integer
'''
class Solution:
    def EvaluatePostfix(self,S):
            object = Evaluate(len(S))
            return (object.evaluatePostfix(S))