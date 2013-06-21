""" Implementation of Insertion Sort in Python """
def sort(list):
    for i in range(0,len(list)-1):
        for j in range(i+1,0,-1):
            if list[j] < list[j-1]:
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp
    return list
ll=[10,2,30,4]
print sort(ll)