'''
QUIZ #2
Name: 
ID: 

Follow the instructions in the comments below. Then upload this file, with your answers, to Omnivox.
'''

import time
# 1. In a new line, with a new command, add a string to this list
games = ["Gloomhaven", "Radlands", "Ethnos", "Res Arcana", "Spirit Island", "Bloc by Bloc", ]
add_strings = 'Quiz03'
games.append(add_strings)
print("The list after appending is: " + str(games))


print('#################################################')
# 2. Loop through the list and print out all string longer than 7.

for game in games:
    if len(game) > 7:
        print(len(game), game)

# 3. Create a function that takes in one number and counts backwards from that number to 0 (printing out each number as it goes)

def count_rounds():
    rounds = 100
    while rounds > 0:
        print(rounds)
        rounds = rounds - 10
        time.sleep(0.5)

# 4. Create a function that takes in a string and returns a list with every other letter in that string
def return_list():
    question = "Create a function that takes in a string and returns a list with every other letter in that string"

    print('#################################################')
    print(question[::2])

# 5. Call the functions you created in questions 3 and 4



count_rounds()
return_list()
