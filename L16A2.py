try:
    num1, num2 = eval(input("input 2 numbers seperated by a comma: "))

    res = num1 / num2
    print("your 2 numbers divided by each other is: ", res)

except ZeroDivisionError:
    print("division by zero is an error :( !!!!!")
except SyntaxError:
    print("this is a SyntaxError :(")
except:
    print("wrong input")
finally:
    print("no mistakes")


