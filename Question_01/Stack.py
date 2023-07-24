import numpy as np


class Stack:
    def __init__(self,limit=7):
        self.limit = limit
        self.stack = []

    def push(self,data): #define push
        if len(self.stack) < self.limit: #check stack len is less than the limit
            return self.stack.append(data) #if it is append a new data to stack
        else:
            print("stack overflow") #else pprint stack is overflow

    def pop(self): #define pop
        if len(self.stack) == 0:
            print("stack underflow") #if stack is empty print stack underflow
        else:
            return self.stack.pop() #delete the value from stack

    def top(self): #define top
        if len(self.stack) == 0:
            print("stack underflow") #if stack is empty print stack is underflow
        else:
            return self.stack[len(self.stack) - 1] #else return the top valuve of the stack

    def isEmptyStack(self): #define whether stack is emty
        return len(self.stack) == 0

    def isFullStack(self): #define whether the stack is full
        return len(self.stack) == self.limit

    def size(self):
        return len(self.stack)