# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# combine both names to one string and lower case it
combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')

true = (t + r + u + e) * 10
print(true)

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')

love = l + o + v + e
print(love)

total_count = true + love

if total_count > 10 or total_count > 90:
    print(f"Your score is {total_count} , you go together like coke and mentos.")
elif total_count >= 40 and total_count <= 50:
    print(f"Your score is {total_count} , you are alright together.")
else:
    print(f"Your score is {total_count}")