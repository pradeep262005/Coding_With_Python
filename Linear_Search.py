def linear_Search(l, n, key):  
  
     
    for i in range(0, n):  
        if (l[i] == key):  
            return i  
    return -1  
  
  
l= [1 ,3, 5, 4, 7, 9]  
key = int(input('ENTER THE NO:'))
  
n = len(l)  
res = linear_Search(l, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)
