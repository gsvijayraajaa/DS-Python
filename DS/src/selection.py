def sort(list):
    for i in range(len(list),0,-1):
        posi=maximum(list[0:i])
        temp=list[i-1]
        list[i-1]=list[posi]
        list[posi]=temp
    return list

def maximum(list):
    max=0
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
            posi = i
    return posi

ll=[1,43,2,23,5]
print sort(ll)