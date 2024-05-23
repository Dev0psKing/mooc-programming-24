# Write your solution here
# Get user input
number = int(input("Please type in a number: "))

# Determine the magnitude
if number < 1000 and number > 100:
    print("This number is smaller than 1000")
    print(f"Thank you!")
elif number > 10 and number < 100:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print(f"Thank you!")
elif number < 10 :
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    print(f"Thank you!")
else:
    # print("This number is equal to or greater than 10")
    print(f"Thank you!")



