print("what would you like to order?")
print("1. Pizza, $10")
print("2. Burger, $8")
print("3. Sandwich, $6")
print("4. Salad, $5")
print("5. Soda, $2")
print("6. Water, $1")

pizza = 10
burger = 8
sandwich = 6
salad = 5
soda = 2
water = 1

input = int(input("enter the number of your order: "))
for i in range(1, 7):
    if input == 1:
        print("you ordered a pizza and your total is: $", pizza)
        break
    elif input == 2:
        print("you ordered a burger and your total is: $", burger)
        break
    elif input == 3:
        print("you ordered a sandwich and your total is: $", sandwich)
        break
    elif input == 4:
        print("you ordered a salad and your total is: $", salad)
        break
    elif input == 5:
        print("you ordered a soda and your total is: $", soda)
        break
    elif input == 6:
        print("you ordered water and your total is: $", water)
        break
    else:
        print("invalid order")