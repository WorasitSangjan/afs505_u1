# Import 'sys' library and call 'argv' function
from sys import argv

# Set the argument for 'argv'
script, input_file = argv

# Create the reading file function
def print_all(f):
    print(f.read())

# Create the setting current function
def rewind(f):
    f.seek(0)

# Create displaying function (show at specific line)
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Set variable by opening the input file
current_file = open(input_file)

# Display information
print("First let's print the whole file:\n")

# Display the inforation in the current file
print_all(current_file)

# Display information
print("Now let's rewind, kind of like a tape.")

# Use the function rewind to set the current position
rewind(current_file)

# Disply information
print("Let's print three lines:")

# Set variable
current_line = 1
# Use the finction print_a_line
print_a_line(current_line, current_file)

# Set variable
current_line = current_line + 1
# Use the finction print_a_line
print_a_line(current_line, current_file)

# Set variable
current_line = current_line + 1
# Use the finction print_a_line
print_a_line(current_line, current_file)
