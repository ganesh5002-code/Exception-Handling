try:
    num1, num2 = eval(input("Enter two numbers seperated by a comma:"))
    result = num1/num2
    print("The result of", num1, "divided by", num2, "is", result)
except ZeroDivisionError:
    print("The second number can't be a zero")
except SyntaxError:
    print("There is no comma separating the numbers")
except:
    print("It is an invalid output")
else:
    print("There are no exceptions")
finally:
    print("This code will execute no matter what")
