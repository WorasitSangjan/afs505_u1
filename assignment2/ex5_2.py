name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk aboout {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Unit converter
inch_to_cm = 2.54
lbs_to_kg = 0.453592
height_cm = round(height * inch_to_cm, 2) # Display only 2 digits
weight_kg = round(weight * lbs_to_kg, 2)
print("Display the height and weight of Mr. Shaw in SI unit")
print(f"He's {height_cm} centimeters tall.")
print(f"He's {weight_kg} kilograms heavy.")
