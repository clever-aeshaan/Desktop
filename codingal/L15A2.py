num = int(input("enter a integer:  "))

if num % 20 == 0:
    print("TWIST")
if num % 15 == 0:
    pass
if num % 5 == 0:
    print("FIZZ")
if num % 3 == 0:
    print("buzz")
else:
    print(num)    