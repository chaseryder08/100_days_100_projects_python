#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password var
password = []

# for loop to randomly select letters in user req and add to password
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
    
# '' for symbols
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
    
# '' for numbers
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)


    
print(password)
random.shuffle(password)
print(password)

hard_pass = ""

for char in password:
    hard_pass += char

print(hard_pass)



'''  
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_pass = ""

len_password = len(password)

for x in range(0, len_password):
    pass_letter_2 = random.choice(password)
    hard_pass += pass_letter_2
    
print(hard_pass)
    




    
pass_num_count = random.randint(0, len_password)
    x = password[pass_num_count]
    password = password.replace(x,"")
    hard_pass.append(x)
    print(password)
    print(hard_pass)

print(hard_pass)

'''