def calculate_difference():
    numbers = []  # Initialize an empty list

    for i in range(10):
        num = int(input(f"Enter num {i + 1}: "))  # Get input
        numbers += [num]  # Add number to the list without using append()

    first_num = numbers[0]
    remaining_sum = sum(numbers[1:])

    return first_num - remaining_sum


# Call the function and print the result
result = calculate_difference()
print("Result:", result)
