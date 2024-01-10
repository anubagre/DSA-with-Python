# Insertion Sort using Recursive Approach
def InsertionSort(l):
    for SliceEnd in range(len(l)):
        pos=SliceEnd
        while pos>0 and l[pos]<l[pos-1]:
            l[pos],l[pos-1]=l[pos-1],l[pos]
            pos=pos-1
    return l
l=[89,74,32,55,21,64]
print(InsertionSort(l))