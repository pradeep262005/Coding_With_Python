str1 = input("Enter a string1:")
str2 = input("Enter a string2:")
x = str1[:2] + str2[2:]
y = str2[:2] + str1[2:]
r = x + " " + y
print(r)
