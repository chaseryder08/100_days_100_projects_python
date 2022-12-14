art = """
_____.___.                                _____                 __       ________                       
\__  |   | ____  __ __  ____    ____     /     \   ____   ____ |  | __  /  _____/_____    _____   ____  
 /   |   |/  _ \|  |  \/    \  / ___\   /  \ /  \ /  _ \ /    \|  |/ / /   \  ___\__  \  /     \_/ __ \ 
 \____   (  <_> )  |  /   |  \/ /_/  > /    Y    (  <_> )   |  \    <  \    \_\  \/ __ \|  Y Y  \  ___/ 
 / ______|\____/|____/|___|  /\___  /  \____|__  /\____/|___|  /__|_ \  \______  (____  /__|_|  /\___  >
 \/                        \//_____/           \/            \/     \/         \/     \/      \/     \/
 
"""
import random

easy_lives = 10
hard_lives = 5

def set_difficulty():
    level = input("Type hard or easy : ".lower())
    if level == "easy":
        turns = easy_lives
        return turns
    elif level == "hard":
        turns = hard_lives
        return turns

#choose difficulty

#compares numbers    
def check_num(user, answer_num):
    if user == answer_num:
        print("YOU WIN!")
        exit()
    elif user > answer_num:
        print("Too high")
        return turns - 1
    elif user < answer_num:
        print("Too low")
        return turns - 1

        


#number generated
answer_num = random.randint(1,101)
print(answer_num)

turns = set_difficulty()

#user input
user = int(input("Guess a number 1-100 : "))
check_num(user, answer_num)


while turns > 0:
    print(f"You have {turns} turns left ...")
    user = int(input("Guess again number 1-100 : "))
    turns = check_num(user, answer_num)
    
print("""
      
  ________    _____      _____  ___________ ____________   _________________________ 
 /  _____/   /  _  \    /     \ \_   _____/ \_____  \   \ /   /\_   _____/\______   \
/   \  ___  /  /_\  \  /  \ /  \ |    __)_   /   |   \   Y   /  |    __)_  |       _/
\    \_\  \/    |    \/    Y    \|        \ /    |    \     /   |        \ |    |   \
 \______  /\____|__  /\____|__  /_______  / \_______  /\___/   /_______  / |____|_  /
        \/         \/         \/        \/          \/                 \/         \/ 
      
      """)
    


