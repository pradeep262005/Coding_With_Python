def mergeSort(a):
    print('splitting',a)
    if len(a)>1:
        mid=len(a)//2
        l=a[:mid]
        r=a[mid:]
        mergeSort(l)
        mergeSort(r)
        i=0; j=0; k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
            k+=1

        while i<len(l):
            a[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            a[k]=r[j]
            j+=1
            k+=1
    print('Merging',a)


a=[15,2,0,48,97]
mergeSort(a)
print(a)
