# Write your solution here
# Get user input
hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_of_week = input("Day of the week: ")

# Calculate daily wages, doubling hourly wage on Sundays
if day_of_week.lower() == "sunday":
    daily_wages = hourly_wage * hours_worked * 2
else:
    daily_wages = hourly_wage * hours_worked

# Print the result
print(f"Daily wages: {daily_wages} euros")
