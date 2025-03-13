def lowest_number():
    # List to store user-entered numbers
    numbers = []

    while True:
        try:
            # Prompt user for input and convert to integer
            num = int(input("Enter a number (or invalid input to stop): "))
            numbers.append(num)  # Store valid numbers in the list
        except ValueError:
            # Stop input loop when an invalid input is entered
            break

    # Check if there are valid numbers before computing the minimum
    if numbers:
        print("Lowest number:", min(numbers))  # Display the smallest number
    else:
        print("No valid numbers entered.")  # Handle case where no valid input was given

# Call the function to execute the program
lowest_number()
