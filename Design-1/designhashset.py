class MyHashSet:

    def __init__(self):
        
        self.length = 1000   #setting the length to 1000 as given in the question
        self.primary = [None]*self.length  ##the value in the primary array is none
        
    def hashkey(self,key:int):
        return key % self.length   #we are finding hashkey to avoid the collision
    
    def doublehash(self,key:int):
        
        return key//self.length      #we are finding hashkey to avoid the collision
        

    def add(self, key: int) -> None:
        hashindex = self.hashkey(key)   #we are calling the function hashkey to find the index 
        
        doublehashindex = self.doublehash(key)   #we are calling the function to find the secondary array index
        
        if self.primary[hashindex] == None: #to check whether there are any values in index
            
            if hashindex ==0:  # if the index index is zero to avoid the integer overflow we are adding 1 to the length
                self.primary[hashindex] = [False]* (self.length +1)
            else:
                self.primary[hashindex] = [False] *self.length
                
        self.primary[hashindex][doublehashindex]= True #changing to true after adding the value
            

    def remove(self, key: int) -> None:
        hashindex = self.hashkey(key)   #we are calling the function hashkey to find the index 
        doublehashindex = self.doublehash(key)  #we are calling the function to find the secondary array index
        if self.primary[hashindex] != None:  #if the hashindex is not equal to none then it means there is a value so to remove we are chaning to false
            self.primary[hashindex][doublehashindex] = False
        
        

    def contains(self, key: int) -> bool:
        hashindex = self.hashkey(key)  #we are calling the function hashkey to find the index
        doublehashindex = self.doublehash(key)    #we are calling the function to find the secondary array index
        if self.primary[hashindex] != None:
            return self.primary[hashindex][doublehashindex] 
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)