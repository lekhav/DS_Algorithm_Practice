class MyQueue:                         #Queue is FIFO
    
    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x):              
        while len(self.s1) != 0:        #Emptying the stack1 to stack2
            self.s2.append(self.s1.pop())  
        self.s1.append(x)               #adding the new element to stack1
        while len(self.s2) != 0:        #appendind remaning elements from s2 to s1
            self.s1.append(self.s2.pop())        
            
    def pop(self):                      
        return self.s1.pop()
     
    def peek(self):                     
        return self.s1[len(self.s1)-1]
    
    def empty(self):
        return self.s1 == []
     
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



# ————————————————————————————————————————————————————————————————————————————————————————————————
class queueUsingStack:
    def __init__(self):
        self.inqueue = []
        self.outqueue = []

    def push(self, x):
        self.inqueue.append(x)

    def pop(self):
        if self.outqueue != []:
            return self.outqueue.pop()
        while self.inqueue != []:
            self.outqueue.append(self.inqueue.pop())
        return self.outqueue.pop() if self.outqueue != [] else -1
            
    def peek(self):
        if self.outqueue != []:
            return self.outqueue[-1]
        while self.inqueue != []:
            self.outqueue.append(self.inqueue.pop())
        return self.outqueue[-1]
        
    def empty(self):
        return self.inqueue==[] and self.outqueue==[]