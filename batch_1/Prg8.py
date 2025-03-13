nums = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
odd_count = sum(1 for num in nums if num % 2 != 0)
print(odd_count)
