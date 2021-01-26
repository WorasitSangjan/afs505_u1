# Set the variable the number of people types
types_of_people = 10
# Set the variable "x" using f-string
x = f"There are {types_of_people} types of people."

# Set the variable "binary" value
binary = "binary"
# Set the variable "do_not" value
do_not = "don't"
# Set the variable "y" using f-string
y = f"Those who know {binary} and those who {do_not}."

# Display variable "x"
print(x)
# Display variable "y"
print(y)

# Display variable "x" using f-string
print(f"I said: {x}")
# Display variable "y" using f-string
print(f"I also said: {y}")

# Set varialbe "hilarious" value
hilarious = False
# Set variable "joke_evaliation"
joke_evaliation = "Isn't that joke so funny?! {}"

# Display "joke_evaliation" using format() syntax
print(joke_evaliation.format(hilarious))

# Set variable "w" value
w = "This is the left side of..."
# Set variable "e" value
e = "a string with a right side."
# Display variable "w" and "e"
print(w + e)
