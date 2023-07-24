class Node:
    def __init__(self):            #initializing node
        self.data = None         #data
        self.Next = None         #next node address field


    # set data of node
    def setData(self, data):
        self.data = data

    # get data of this node
    def getData(self):
        return self.data

    # set next of the node
    def setNext(self, next):
        self.Next = next

    # get data of this node
    def getNext(self):
        return self.Next


class Stack:
    def __init__(self,limit):

        self.head = None
        self.limit = limit
        self.length = 0

    def isEmptyStack(self):    #define whether the stack is empty
                              # by checking the head node
        if self.head is None:
            print("Stack Underflow")

    def isFullStack(self):           #define whether the stack is full
                                #by checking the length of stack and limit of stack are equal
        if self.length == self.limit:
            print("Stack Overflow")



    def push(self,data):

        if self.length < self.limit:
            newNode = Node()  # creating the new  node
            newNode.setData(data)  # set user data for the new node

            if self.head is None:  # check weather the list is empty
                self.head = newNode  # if it is empty, newnode add as the list's first node

            else:
                newNode.setNext(self.head)  # head node set as newnode's next reference

                self.head = newNode  # now newnode become the head node
            self.length += 1

        else:
                return self.isFullStack()

    def pop(self):  #define pop
        if  self.head is not None:  # check weather the list is not empty
            popNode = self.head.getData() #get deleting data
            self.head = self.head.getNext() #if so self head point to next reference
            self.length -= 1
            return popNode  #return deleted value

        else:
            return self.isEmptyStack()

    def top(self): #define top
        if self.length != 0:    #check the stack length
            return self.head.getData()    #return the self.head's data as the top value
        else:
            return self.isEmptyStack()

    def size(self):  #deine size
            return self.length
