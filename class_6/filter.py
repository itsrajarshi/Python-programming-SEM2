# List of names
names = ['johy', 'james', 'jimmy']

# Function to check name length
def is_long_name(name):
    return len(name) > 4

# Filter names longer than 4 characters
filtered_names = list(filter(is_long_name, names))

# Display result
print("Filtered names:", filtered_names)