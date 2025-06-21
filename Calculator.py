num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

print("Choose an operator")
operator = input("Enter the operator : ")

if operator == '+':
    result = num1 + num2
    print("Result : ", result)
elif operator == '-':
    result = num1 - num2
    print("Result : ", result)
elif operator == '*':
    result = num1 * num2
    print("Result : ", result)
elif operator == '/':
    if num2!= 0:
        result = num1 / num2
        print("Result : ", result)
    else:
        print("Error : Cannot divide by zero.")
else:
    print("Invalid choice of operator")


