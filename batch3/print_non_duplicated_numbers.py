def no_duplicate_numbers():
    # List to store user-entered numbers
    numbers = []

    print("Enter 10 numbers:")
    for nums in range(10):
        # Prompt user for input and convert to integer
        num = int(input(f"Enter number {nums + 1}: "))
        numbers.append(num)  # Store numbers in the list

    # Filter numbers that appear only once in the list
    unique_nums = [num for num in numbers if numbers.count(num) == 1]

    print("Numbers without duplicates:", unique_nums)  # Display unique numbers

# Call the function to execute the program
no_duplicate_numbers()
