def highest_number():
    numbers = []  # List to store user-entered numbers

    while True:
        try:
            num = int(input("Enter a number (or invalid input to stop): "))
            numbers.append(num)  # Add valid numbers to the list
        except ValueError:
            break  # Stops when invalid input is entered

    if numbers:
        print("Highest number:", max(numbers))  # Display the highest number
    else:
        print("No valid numbers entered")  # Handle empty input case

highest_number()
