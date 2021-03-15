class queueUsingStack:
    def __init__(self):
        self.inQueue = []
        self.outQueue = []
        
    def push(self, x):
        self.inQueue.append(x)
        
    def fillOutQueue(self):
        l = len(self.inQueue)
        while l > 0:
            self.outQueue.append(self.inQueue.pop())
            l -= 1

    def pop(self):
        if len(self.outQueue) == 0:
            self.fillOutQueue()
        return self.outQueue.pop() if len(self.outQueue) != 0 else -1

    def peek(self):
        if len(self.outQueue) == 0:
            self.fillOutQueue()
        return self.outQueue[-1] if len(self.outQueue) != 0 else -1
            
    def empty(self):
        if len(self.inQueue) == 0 and len(self.outQueue) == 0:
            return True
        return False


# ————————————————————————————————————————————————————————————————————————————————————————————————


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