try:
 numerator = 10
 denominator = 5
 result = numerator/denominator
 print(result)
except ZeroDivisionError:
 print("Error: Denominator cannot be 0.")
 
finally:
 print("This is finally block.")
