import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock, paper, scissors]

user_choice = int(input("Choose Rock - 0 , Paper - 1, or scissors - 2 : "))
comp_choice = random.randint(0, 2)

if user_choice == 0 and comp_choice == 1:
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[comp_choice])
    print("You lose")
elif user_choice == 0 and comp_choice == 2:
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[comp_choice])
    print("You win!")
elif user_choice == 0 and comp_choice == 0: 
    print("DRAW!")
    
if user_choice == 1 and comp_choice == 2:
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[comp_choice])
    print("You lose!")
elif user_choice == 1 and comp_choice == 0:
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[comp_choice])
    print("You win")
elif user_choice == 1 and comp_choice == 1: 
    print("DRAW!")
    
if user_choice == 2 and comp_choice == 0:
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[comp_choice])
    print("You lose")
elif user_choice == 2 and comp_choice == 1:
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[comp_choice])
    print("You win!")
elif user_choice == 2 and comp_choice == 2: 
    print("DRAW!")

