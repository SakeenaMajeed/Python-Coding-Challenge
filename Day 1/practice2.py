import os

# Specify the directory path
directory_path = "/sakeena"  # Replace this with the actual directory path

# Get the list of all entries in the directory
entries = os.listdir(directory_path)  # Corrected the function call

# Iterate over the entries and print them
for entry in entries:
    print(entry)