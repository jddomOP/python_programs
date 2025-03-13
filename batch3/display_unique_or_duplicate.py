def unique_or_duplicate():
    # List to store unique numbers entered by the user
    numbers = []

    while True:
        try:
            # Prompt user for input and convert to integer
            num = int(input("Enter a number: "))

            # Check if the number is already in the list
            if num in numbers:
                print("Duplicate")  # Notify user of duplicate entry
            else:
                print("Unique")  # Notify user of unique entry
                numbers.append(num)  # Add unique number to the list

        except ValueError:
            # Break the loop if the user enters a non-integer value
            break

# Call the function to start the input process
unique_or_duplicate()
