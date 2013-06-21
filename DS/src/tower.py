""" Implementation of Tower Of Hanoi in Python """
def moveTower(height,s,d,i):
    if height >= 1:
        moveTower(height-1,s,i,d)
        moveDisk(s,d)
        moveTower(height-1,i,d,s)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(5,"A","B","C")