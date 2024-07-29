var1 = input("Please Enter First String : ") 
var2=input("Please Enter Second String : ")
x=var1[0:2]
var1=var1.replace(var1[0:2],var2[0:2]) 
var2=var2.replace(var2[0:2],x) 
print("Your  string has changed into :",var1,'',var2) 


 
