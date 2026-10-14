try:
    num = int(input("enter a number:  "))
    print("your number is:", num)
except ValueError as x:
    print("this is a", x)
    