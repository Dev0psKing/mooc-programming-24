# Write your solution here
# Get user input
temperature_f = float(input("Please type in a temperature (F): "))

# Convert Fahrenheit to Celsius using the formula: (F - 32) * 5/9
temperature_c = (temperature_f - 32) * 5/9

# Print the converted temperature in Celsius
print(f"{temperature_f} degrees Fahrenheit equals {temperature_c} degrees Celsius")

# Check if it's below zero degrees Celsius
if temperature_c < 0:
    print("Brr! It's cold in here!")
