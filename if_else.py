height = int(input("How tall are you? : "))
bill = 0

if height >= 120:
    print("You can ride")
    age = int(input("What is your age? : "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <=18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("You are going through mid life crisis - you can ride for free!")
    else:
        bill = 12
        print("Pay full adult price - $12")
    
    while True:
        want_photo = input("Do you want a photo taken - Y or N : ").capitalize()
        if want_photo == "Y":
            bill += 3
            break
        elif want_photo == "N":
            print("No photo added to bill")
            break
        else:
            print("Invalid entry")
    
    print(f"Your total bill is {bill}")
                
        
else:
    print("Sorry, you must be 120cm and +18 to ride.")