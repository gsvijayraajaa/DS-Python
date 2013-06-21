""" Implementation of Bubble sort in Python """
class bubble():
    def __init__(self,ll):
        self.l=ll
    def sort(self):
        for iter in range(len(self.l)-1,0,-1):
            for i in range(iter):
                if self.l[i] > self.l[i+1]:
                    temp = self.l[i]
                    self.l[i] = self.l[i+1]
                    self.l[i+1] = temp
        return self.l
        
ll=[10,2,15,4]
b = bubble(ll)
print b.sort()
