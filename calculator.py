def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


operation = input(
    "***Addition - Subtraction - Multiplication - Division***\nSelect the operation you need to do: "
)
Fnum = float(input("Enter the First number: "))
Snum = float(input("Enter the Second number: "))

if operation.lower() == "addition":
    print(addition(Fnum, Snum))
elif operation.lower() == "subtraction":
    print(subtraction(Fnum, Snum))
elif operation.lower() == "multiplication":
    print(multiplication(Fnum, Snum))
elif operation.lower() == "division":
    print(division(Fnum, Snum))
else:
    print("Error")
