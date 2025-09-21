# finding an error in a program
try:
    num = int(input("Enter a number:"))
    print(num, "is valid")
except ValueError as x:
    print("Exception:", x)



