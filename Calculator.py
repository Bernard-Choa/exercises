num1 = int(input("Enter 1st number: "))
operator = input("Enter arithmetic operator")
num2 = int(input("Enter 2nd number"))

if "+" in operator:
    print(num1 + num2)

elif "-" in operator :
    print(num1 - num2)

elif "*" in operator:
    print(num1 * num2)

elif "/" in operator:
    print(num1 / num2)

elif "//" in operator:
    print(num1 // num2)

elif operator == "**":
    print(num1 ** num2)

else:
    print("Operator invalid")