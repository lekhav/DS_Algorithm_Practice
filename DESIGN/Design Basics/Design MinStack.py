# Implement a Stack with O(1) : push, pop, top, getMin operations in O[1] Time
# Design a Data Structure SpecialStack that supports all the stack operations 
# push(), pop(), isEmpty(), isFull(), getMin() which should return minimum element from the SpecialStack. 
# you should only use standard Stack data structure and no other data structure like arrays, list, .. etc. 



# using 1 stack, 1 variable
# O[N] Space, O[1] Time
class MinStack_OPTIMIZED:
    def __init__(self):
        self.st = []
        self.minVal = float('inf')

    def push(self, x):
        if x <= self.minVal:
            self.st.append(self.minVal)
            self.minVal = x
        self.st.append(x)

    def pop(self):
        poppedVal = self.st.pop()
        if poppedVal == self.minVal:
            self.minVal = self.st.pop()

    def top(self):
        return self.st[-1]
        
    def getMin(self):
        return self.minVal
        



# using 2 Stacks, O(2N) space
# O[2N] Space, O[1] Time
class MinStack:
    def __init__(self):
        self.st = []
        self.minSt = [float('inf')]

    def push(self, x):
        self.st.append(x)
        self.minSt.append(min(self.minSt[-1], x))

    def pop(self):
        self.st.pop()
        self.minSt.pop()

    def top(self):
        return self.st[-1]
    
    def getMin(self):
        return self.minSt[-1]





