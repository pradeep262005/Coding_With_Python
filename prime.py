n=int(input('Enter the no:'))
for num in range(1,n+1):
    for i in range(2,num):
        if (num%i==0):
            print(num,'is not prime')
            break
        else:
            print(num,'is prime')
            break

