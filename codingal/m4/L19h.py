user_input = input("Enter numbers separated by spaces: ")
userlist = user_input.split()
evenlist = []
oddlist = []

i = 0
while i < len(userlist):
    num = int(userlist[i])
    par = num % 2
    if par == 0:
        evenlist = evenlist + [num]
    else:
        oddlist = oddlist + [num]
    i = i + 1

print("all the even numbers are: ", evenlist)
print("all the odd numbers are: ", oddlist)