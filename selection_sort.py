def SelectionSort(l):
    for start in range(len(l)):
        minpos=start
        for i in range(start,len(l)):
            if l[i]<l[minpos]:
                minpos=i
        print(start,minpos)
        l[start],l[minpos]=l[minpos],l[start]
    return l
l=[89,74,32,55,21,64]
print(SelectionSort(l))