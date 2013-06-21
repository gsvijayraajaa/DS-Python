""" Implementation of LinkedList in Python """
class linked():
    def __init__(self,data):
        self.right=None
        self.val=data
    def app(self,data):
        current = self
        while current.right:
            current = current.right
        current.right=linked(data)
    def insert(self,position,data):
        current = self
        for i in range(position):
            current = self.right
        next = current.right
        current.right=linked(data)
        current.right.right = next
        
    def __str__(self):
        return "(%s,%s)" %(self.val,self.right) 
    def show(self):
        if self.right != None:
            print self.val
            self.right.show()

l = linked(1)
l.app(2)
l.app(3)
l.app(4)
l.insert(3,10)
print l