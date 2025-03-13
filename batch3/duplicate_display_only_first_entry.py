def duplicate_show_first_entry():
    # List to store user-entered numbers in order
    numbers = []

    # Set to track numbers that have been seen
    seen = set()

    print("Enter 10 numbers:")
    for nums in range(10):
        # Prompt user for input and convert to integer
        num = int(input(f"Enter number {nums + 1}: "))

        # If number is not in seen set, add it
        if num not in seen:
            seen.add(num)  # Track first occurrence
        numbers.append(num)  # Store all numbers entered

    print("Filtered numbers (keeping first occurrence of duplicates):")

    # List to store filtered numbers
    result = []

    for num in numbers:
        if num in seen:
            result.append(num)  # Keep first occurrence
            seen.remove(num)  # Ensure only first occurrence is kept

    print(result)  # Display filtered list


# Call the function to execute the program
duplicate_show_first_entry()

