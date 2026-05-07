# calculator project

# taking numbers
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

op = (input("Enter operation (+,-,*,/) : "))

# checking operation

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("INVALID OPERATION")