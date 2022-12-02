# round function
print(round(2.55232334, 2))

# floor division
print(8 // 3)

# f strings
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}. Your height is {height}, and you are {isWinning}")

## F strings automatically convert variables to string

# CONDITIONALS / IF/ELSE

## Nested if/else
if condition
    if another condition:
        do this
    else:
        do this
else:
    do this

### Elif - can list as many as you'd like
if condition 1
    do a
elif:
    do b
else: 
    do c

# Logical operators
> AND - OR - NOT


## print(''' asdasdasdasdas ''')
> as with comments, use ''' to print out multiple lines ''' )

## \ will tell python to ignore
> print("You\'re a man")

# Day 4
* random module
* random.randint(0, 1)
  > will pick number between 0 and 1
* random.choice() 
  > will randomly pick item in list/tuple

### unable to memorize every method
> can't store -- need ot just know how to use code
> when new thing -- google search documentation to read through what you can do...
> learn what is possible ... USE GOOGLE

## PROGRAMMING ISN"T OPEN ENEDED! Just need ot learn how to search and figure it out!

*********************

# Day 6
FUNCTIONS:

* len()
* print()
* range()

## PRO TIP:>
> to indent code -> hold CTRL + ] or [
> moves code block!


# WHILE

while not at_goal():
    jump()

or while at_goal() != True:
    jump()



# FLOW CHART > important
> draw out step by step how program will work
> rectangle - input(jobs
> <> diamond - while loops

## For loops 
list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
list.reverse() -- reverses the list in place (does not return it)
list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).

# DAY 8
## Functions
def greet_with_name(name):
  print(f"hi {name}")
  print(f"How do you like {name}?")
  print(f"What is your favorite movie {name}?")

PARAMETERS inside function runs
parameter we are creating a new function

### paramter - name of data !
### argument - value of data !

## Can store multiple paramters
### Arguments are positional unless using KEYWORD ARG
def greet_with(name, location):
    print(f"Hello {name}, you are located in {boston}")

greet_with("Chase, "Boston")

## KEY WORD ARG 
> if switch lcation of param still will call but code is longer

my_function(a=1, b=2, C=3)

### math function to round up highest
import math

math.ciel(area)