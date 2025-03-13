numbers = []

while True:
    try:
        num = int(input("Enter a number (or invalid input to stop): "))
        numbers.append(num)
    except ValueError:
        break  # Stop when invalid input is entered

    if numbers:
        numbers.sort()  # Sorts the numbers in ascending order
        print("Sorted numbers:", numbers)
    else:
        print("No valid numbers entered.")