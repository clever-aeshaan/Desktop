buy = int(input("enter buying value: "))
sell = int(input("enter selling value:  "))

result = sell - buy

if(result>0):
    print("you made profit! :)")
else:
    print("you made loss :(")