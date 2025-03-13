def duplicate_numbers():
    numbers = []  # Store user-entered numbers

    print("Enter 10 numbers: ")
    for nums in range(10):
        num = int(input(f"Enter number {nums + 1}: "))
        numbers.append(num)  # Collect input

    # Find duplicate numbers and sort them
    duplicates = sorted(set(num for num in numbers if numbers.count(num) > 1))

    if duplicates:
        print("Numbers that have duplicates:", duplicates)
    else:
        print("None")  # No duplicates found

duplicate_numbers()
