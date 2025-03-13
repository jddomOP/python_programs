def highest_lowest():
    numbers = []  # List to store user-input numbers

    while True:
        try:
            num = int(input("Enter a number (or invalid input to stop): "))
            numbers.append(num)  # Store valid numbers
        except ValueError:
            break  # Stop on invalid input

    if numbers:
        numbers.sort(reverse=True)  # Sort in descending order
        print("Numbers sorted from highest to lowest:")
        print(numbers)
    else:
        print("No valid numbers entered.")  # Handle empty input

highest_lowest()
