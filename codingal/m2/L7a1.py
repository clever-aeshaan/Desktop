m = input("do you have a medical condition if yes put y if no put n ")

if(m=='y'):
    print("you cannot write this exam")
else:
    a = int(input("put your attendance number "))
    if(a>75):
        print("you are allowed to write this exam")
    else:
        print("you are not allowed to write this exam")