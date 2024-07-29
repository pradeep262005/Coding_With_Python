a = input("Please Enter First String : ") 
b=input("Please Enter Second String : ")
x=a[0:2] 
a=a.replace(a[0:2],b[0:2]) 
b=b.replace(b[0:2],x) 
print("Your first string has become :- ",a)
print("Your second string has become :- ",b)
