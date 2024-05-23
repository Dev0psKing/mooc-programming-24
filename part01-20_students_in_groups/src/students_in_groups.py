# Write your solution here
import math
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
group = number1 / number2
final = math.ceil(group)
print(f'Number of groups formed: {final}')
# if group % 2 == 0:
#     print()
