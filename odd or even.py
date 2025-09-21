try:
    num = int(input("Enter your age as a whole number:"))
    if num%2 ==0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")
except ValueError:
    print("You have used a decimal point or an alphabet or special character in your output")
else:
    print("There are no errors in your output")
finally:
    print("This code will execute no matter what")

