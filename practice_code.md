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

# DICTIONARY
* {key: value, key: value}
* programming_dict["Bug"] - this is how you call specifc parts are dict
* you list the key , not index

bugs = {
    "Butterfly": "jkashdaskljdsa",
    "Grasshopper": "green thing",
}

bugs["Butterfly"]

#Adding new items to dictionary
bugs["Loop"] = "This is what a loop is"

> good idea to create empty dict = {}

empty_dict = {}

## Edit dictionary
>edit file, if not there will create new item
bugs["Butterfly"] = new value


## loop through dictionary
for thing in programming_dict:
    print(thing)

> this will print out all keys

# Nesting dictionary
{ 
    Key: [list],
    Key2: {Dict},
}

can put list and dictionaries INSIDE dict

Dictionary called by KEY name
List called by index number

#Dictionary in a list

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Nice", "Lille"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg"], 
        "total_visits": 6
        },
]

# Day 10

functions

we have :

def func():

def func_mult(result):
    result = 3*2
    return result

var_mic = func_mult(result)

def format_name(f_name, l_name):
    if f_name = "" or l_name == "":
        return "not a valid entry"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {f_name}, {l_name}"

print(format_name(input("Type in your name", "type in your second name"))
    
# DOCSTRINGS
> """ comments extended - will also show documentation """
>
> def doc_string_func():
>   """ this is my doc string """

This will show info
It can also be used for comments

# Return vs Print()
RETURN will end if statement

if user_scire == 0:
 return "you win"
elif computer = 21
    r