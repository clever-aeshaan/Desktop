number = int(input("enter a positive number: "))

if number == 0:
    binary_result = "0"
else:
    binary_result = ""
    while number > 0:
        remainder = number % 2
        binary_result = str(remainder)+binary_result
        number = number // 2

print("the binary version is", binary_result)