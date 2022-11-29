# This program tells us how many days, 
# weeks, months we have left in life is we 
# live until 90 years old

# 365 d/yr
# 52 wk/yr
# 12m/yr

# TO DO Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
''' It will take your current age as the input 
and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

'''
age = int(input("How old are you? : "))
years_remaining = 90 - age
print(years_remaining)
days = years_remaining * 365
weeks = years_remaining * 52
months = years_remaining * 12

message = (f"You have {days} days, {weeks} weeks, and {months} months left.")
print(message)

print(6 + 4 / 2 - (1 * 2))
