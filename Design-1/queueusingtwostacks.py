class MyQueue:

    def __init__(self):
        
        self.instack=[]  # initializing the first stack
        self.outstack=[]  # initializing the out stack
        

    def push(self, x: int) -> None:
        self.instack.append(x)  # appending the values in instack
        

    def pop(self) -> int:
        temp = self.peek()  #we are calling the peek function and storing the returned value in temp variable
        self.outstack=self.outstack[:-1] # we are removing the last element
        return temp  #returning the temp
        

    def peek(self) -> int:
        if len(self.outstack)==0:  #if the outstack is empty
            while self.instack:
                element = self.instack.pop() # we are popping the elements from isnatcka nd storing it in a variable
                self.outstack.append(element) #move the stored value to outstack
        return self.outstack[-1]  #returning the last value of the outstack
                
            
        
        

    def empty(self) -> bool:
        return len(self.instack) + len(self.outstack)==0  #if the length is 0 true will be returned if not false will be returned


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()