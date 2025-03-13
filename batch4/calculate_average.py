def average():
    numbers = []  # Store user-entered numbers

    while True:
        try:
            num = int(input("Enter a number (or invalid input to stop): "))
            numbers.append(num)  # Add valid input to list
        except ValueError:
            break  # Stop when an invalid input is entered

    if numbers:
        avg = sum(numbers) / len(numbers)  # Calculate average
        print("Average:", avg)
    else:
        print("No valid numbers entered")  # Handle empty input case

average()
