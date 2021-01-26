# Set the format syntax
formatter = "{} {} {} {}"

# Display the format passing the int value
print(formatter.format(1, 2, 3, 4))
# Display the format passing the str value
print(formatter.format("one", "two", "three", "four"))
# Display the format passing the boolean value
print(formatter.format(True, False, False, True))
# Display the format passing the setting value
print(formatter.format(formatter, formatter, formatter, formatter))
# Display the format passing the str value
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
