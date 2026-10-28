num = int(input(" enter a number"))

digit = 0

if num == 0:
    digit = 1
else:
    while num > 0:
            num = num//10
            digit += 1
print("the amount is", digit)