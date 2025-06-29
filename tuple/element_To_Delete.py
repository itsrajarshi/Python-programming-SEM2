# Read a tuple from the user
t = tuple(input("Enter elements of the tuple separated by space: ").split())

# Read the element to delete
item_to_delete = input("Enter the element to delete: ")

# Convert to list to perform deletion
t_list = list(t)

if item_to_delete in t_list:
    t_list.remove(item_to_delete)
    new_tuple = tuple(t_list)
    print("Tuple after deletion:", new_tuple)
else:
    print("Element not found in the tuple.")