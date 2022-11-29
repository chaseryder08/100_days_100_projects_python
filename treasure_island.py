print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
# First entry 
cross_road = input("You see a bridge, but it appears to be dangerous -- Do you want to cross it or go around? \n Type 'cross' or 'go around' : ").lower()
if cross_road == "go around":
    moat = input("You walk around the bridge, but realize you need to either swim across or swing from a vine -- Type 'swim' or 'swing': ").lower()
    if moat == "swing":
        gate = input("You swing across the moat and dodge a crocodile -- NOW! You see a big door -- Do you open it or shit your pants? -- type 'shit' or 'open' : ").lower()
        if gate == "shit":
            print("You a bitch. You lose")
        elif gate == "open":
            print("You\'re a bad ass mofo. You bang the girl -- YOU WIN! \n")
            print('''
            *************************************
                    .,^v,
                    ;;.  |---.
                ;;:;  \~/ /
                ;;;;'~  ~\/
                ;;;/ ,  \ \
                `;/ /:  _)_)
                / /;'  ./____
            ------/ /-/   -.     \----------.
            __/ /  \     ~-..  \          \
            `~ ~~    `--.._   ). \          \
            - - - - - - - - :  /- \ \ - - - - -.
                            | /   (_ \_        |
                        / /      ~--~       |
            `' `' `' `' `'(  \`' `' `' `' `' `'
                        ~._\           \_/)
            *************************************
            ''')
    else:
        print("You swam and got eaten by a croc")
else:
    print("YOU DIED -- GAME OVER")
        

