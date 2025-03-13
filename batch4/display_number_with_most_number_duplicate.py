numbers = []

while True:
    try:
        num = int(input("Enter a number (or invalid input to stop): "))
        numbers.append(num)
    except ValueError:
        break  # Stop when invalid input is entered

if numbers:
    unique_numbers = set(numbers)  # Get numbers numbers
    max_count = 0
    most_frequent = []

    for num in unique_numbers:
        count = numbers.count(num)  # Count occurrences of each number
        if count > max_count:
            max_count = count
            most_frequent = [num]
        elif count == max_count:
            most_frequent.append(num)

    print("Number(s) with the most duplicates:", most_frequent)
else:
    print("No valid numbers entered.")