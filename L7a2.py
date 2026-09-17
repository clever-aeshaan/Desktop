x = int(input("how many units of electricity do you use  "))

if(x<=50):
    print("you will need to pay",2*x , "rupees")
else:
    if(x<100):
        print("you will need to pay",100 + (x-50)*3 , "rupees")
    else:
        print("you will need to pay",250 + (x-100)*4 , "rupees")