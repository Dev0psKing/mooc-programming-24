# Get user input
meals_per_week = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
grocery_spending_weekly = float(input("How much money do you spend on groceries in a week? "))

# Calculate average food expenditure
daily_expenditure = (meals_per_week * lunch_price + grocery_spending_weekly) / 7
weekly_expenditure = meals_per_week * lunch_price + grocery_spending_weekly

# Display the results in the expected format
print(f"Average food expenditure:")
print(f"Daily: {daily_expenditure} euros")
print(f"Weekly: {weekly_expenditure} euros")
