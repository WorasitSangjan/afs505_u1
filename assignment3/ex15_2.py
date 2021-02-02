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
