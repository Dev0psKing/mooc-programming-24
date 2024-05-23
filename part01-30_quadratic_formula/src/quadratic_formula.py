from math import sqrt

# Get user input for coefficients
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if roots are real
if discriminant >= 0:
    # Calculate the roots
    root1 = (-b + sqrt(discriminant)) / (2*a)
    root2 = (-b - sqrt(discriminant)) / (2*a)

    # Print the roots
    print(f"The roots are {root1:.2f} and {root2:.2f}")
else:
    print("The equation has complex roots.")
