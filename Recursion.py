def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

num = 10
print("The sum is",recur_sum(num))
