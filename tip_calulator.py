# request bill amount
bill = float(input("How much was the bill? : $"))

# request number of peeps
people = int(input("How many people are splitting the bill?"))

# request tip amount
tip = int(input("How much tip would you like to leave? - 10%, 12%, 15%, 20% :  "))

bill_with_tip = tip / 100 * bill + bill
total_per_person = bill_with_tip / people
final_amount = round(total_per_person, 2)
print(f"Each person will need to pay ${final_amount}")
