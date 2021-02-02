# Create a function for the number of cheese and crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Display the sentence witht the number of cheeses
    print(f"You have {cheese_count} cheeses!")
    # Display the sentence witht the number of crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # Display information
    print("Man that's enough for a party!")
    # Display information
    print("Get a blanket.\n")

# Display another way to fill in the input in function
print("We can just give the function numbers directly:")
# Put the number in the function
cheese_and_crackers(20, 30)

# Display another way to fill in the input in function
print("OR, we can use variables from our script:")
# Set the variable
amount_of_cheese = 10
# Set the variable
amount_of_crackers = 50

# Put the variables in the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Display another way to fill in the input in function
print("We can even do math inside too:")
# Put the math in the function
cheese_and_crackers(10 + 20, 5 + 6)

# Display another way to fill in the input in function
print("And we can combine the two, variables and math:")
# Put the variables and math in the function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
