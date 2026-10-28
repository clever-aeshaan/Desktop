money = int(input("enter how many rupees you want to widthdraw from the ATM  "))

n_100 = (money//100)
n_50 = (money%100)//50
print("you will get ", + n_100,"100s")
print("And you will get", + n_50,"50s")