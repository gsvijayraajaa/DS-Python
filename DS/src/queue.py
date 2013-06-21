class Queue():
    def __init__(self):
        self.items=[]
    def enqueu(self,item):
        self.items.append(item)
    def dequeu(self):
        return self.items.pop(0)
q = Queue()
q.enqueu(1)
q.enqueu(2)
q.enqueu(3)
q.enqueu(4)
q.dequeu()
q.dequeu()
print q.items