#Get the input from user and do some basic calculation
operator = input("Enter anyone of the operator [+,-,*,/] : ")
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

if operator == "+" :
   result = num1 + num2
   print(round(result))
elif operator == "-" :
   result = num1 - num2
   print(round(result))
elif operator == "*" :
   result = num1 * num2
   print(round(result,2))
elif operator == "/" :
    result = num1 / num2
    print(round(result, 2))
else:
    print(f"This {operator} is not a valid opertaor")