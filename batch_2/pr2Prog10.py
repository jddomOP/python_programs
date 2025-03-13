num1 = int(input ("Enter first number:"))
num2 = int (input ("Enter second number:"))

if num1 > num2:
    num1, num2 = num2, num1

for numbers in range (num1 + 1, num2):
    print(numbers)
