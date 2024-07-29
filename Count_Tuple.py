num = [10,20,30,135,76,(10,20),40]
ctr = 0
for n in num:
    if isinstance(n, tuple):
        break
    ctr += 1

print('Count of elements in a list until element is a tuple :',ctr)
