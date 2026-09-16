a=19
b=23
c=14
s=a+b+c
d=b-a-c
if(s>50 and d<0):
    print("The sum is greater than 50 and the difference is negative")
else:
    print("The sum is not greater than 50 or the difference is not negative")
if(s>50 or d<0):
    print("The sum is greater than 50 or the difference is negative")
else:
    print("The sum is not greater than 50 and the difference is not negative")
if(not(s>50 or d<0)):
    print("Neither the sum is greater than 50 nor the difference is negative")
else:
    print("Either the sum is greater than 50 or the difference is negative")
