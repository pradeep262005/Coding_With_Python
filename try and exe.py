while True:
    try:
        x=int(input())
        y=int(input())
        result = x //y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
