{account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take user guess and follower counts and retun if it is right"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

#Make Game repeatable
while game_should_continue:
  #Generate a random account from the game data
  account_a = account_b
  account_b = random.choice(data)  
  
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Compare B: {format_data(account_b)}.")  
  
  # Ask user for a guess
  guess = input("Who has more followers? Guess A or B : ").lower()
  
  #Check if user is correct
  #Get follower account
  a_follower_account = account_a["follower_count"]
  b_follower_account = account_b["follower_count"]
  ##Check follow count for each account
  ##Use if statement to check if user is correct
  
  is_correct = check_answer(guess, a_follower_account, b_follower_account)
  #Clear screen
  clear()
  print(logo)
  
  #Give user feedback on their guess
  if is_correct:
    #Score keeping
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    game_should_continue = False
    print(f"Sorry, you're wrong - Final score {score}")

    
  #Clear Screen

