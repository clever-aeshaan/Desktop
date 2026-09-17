temp = int(input("enter the temp outside in fahrenheit: "))

if(temp<50):
    print("you need a coat and snow gear")
elif(temp<80 and temp>50):
    print("you need a sweat shirt and pants")
elif(temp<100 and temp>80):
    print("you need a short-sleeve shirt and shorts")
else:
    print("don't go outside")