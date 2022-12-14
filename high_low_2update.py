from art import logo, vs
from game_data import data
import random
import replit


#TODO break down into steps
#Start easiest to hardest

score = 0

#print logo
print(logo)


#Select random items in game_data list
def random_choice():
    choice = random.choice(data)
    return choice
    
choice_A = random_choice()
choice_B = random_choice()

#Print choice A
print(f"Compare A: {choice_A['name']}, {choice_A['description']}, from {choice_A['country']}.")

#print VS
print(vs)

#Print choice B
print(f"Compare B: {choice_B['name']}, {choice_B['description']}, from {choice_B['country']}.")

#Input user to select A or B
select = input("Who has more followers? Type 'A' or 'B': ").capitalize()

#Compare A and B
def compare_choices(choice_A, choice_B):
  if select == "A":
    if choice_A['follower_count'] > choice_B['follower_count']:
      return score + 1
    else:
      print("You're wrong -- you lose")
      exit()
  elif select == "B":
    if choice_B['follower_count'] > choice_A['follower_count']:
      return score + 1
    else: 
      print("You're wrong -- you lose")
      exit()
    
result_score = compare_choices(choice_A, choice_B)
print(score)

game_over = False
while not game_over:
  replit.clear()
  print(logo)
  print(f"You're right! Current score: {score + 1}")
  if select == "A":
    choice_A = choice_A
  else:
    choice_A = choice_B

  print(f"Compare A: {choice_A['name']}, {choice_A['description']}, from {choice_A['country']}.")
  
  #print VS
  print(vs)

  choice_B = random_choice()
  print(f"Compare B: {choice_B['name']}, {choice_B['description']}, from {choice_B['country']}.")

  #Input user to select A or B
  select = input("Who has more followers? Type 'A' or 'B': ").capitalize()
  
  answer = compare_choices(choice_A, choice_B)
  print(answer)
  
  

#if correct, on top presents score
#print(f"You're right! Current score: {score}")
