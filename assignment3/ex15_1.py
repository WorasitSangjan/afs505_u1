# Import 'argv' from 'sys'library
from sys import argv

# Declare the file for 'argv'
script, filename = argv

# Open the input file
txt = open(filename)

# Display the input filename
print(f"Here's your file {filename}:")
# Read and display the information in inputfile
print(txt.read())
txt.close()

# Display information
print("Type the filename again")
# Ask for the input filename
file_again = input(">")

# Opent the input file
txt_again = open(file_again)

# Read and dispaly the information in inputfile
print(txt_again.read())
tex_again.close()
