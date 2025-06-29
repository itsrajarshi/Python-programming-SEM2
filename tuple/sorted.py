# Input: number of tuples
n = int(input("Enter the number of tuples: "))
tuple_list = []

# Read each tuple
for _ in range(n):
    elements = input(f"Enter elements of tuple {_+1} separated by space: ").split()
    # Convert elements to integers (or keep as str if needed)
    tuple_list.append(tuple(map(int, elements)))

# Sort the list of tuples
tuple_list.sort()

# Output the sorted list
print("Sorted list of tuples:", tuple_list)