import random
choices = ["rock", "paper", "scissors"]
x = random.choice(choices)
user_input = input("enter rock or paper or scissors : ").lower()
print(f'computer_choice is {x}\nuser_input is {user_input}')
if x != user_input:
    print("you lose")
else:
    print("you win")
