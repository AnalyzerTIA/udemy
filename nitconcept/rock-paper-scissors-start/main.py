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
# import random
# print("Welcome to Rock, Paper, Scissors!")
# print("What is your name?")
# name = input()
# print("Hello, " + name + "!")
# print("What is your move? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
# move = int(input())
# if move == 0:
#     print(rock)
# elif move == 1:
#     print(paper)
# else:
#     print(scissors)
# print("Computer's move:")
# computer_move = random.randint(0,2)
# if computer_move == 0:
#     print(rock)
# elif computer_move == 1:
#     print(paper)
# else:
#     print(scissors)
# if move >= 3 or move < 0:
#     print("You typed an invalid number!")
# elif move == computer_move:
#     print("It's a tie!")
# elif move == 0 and computer_move == 1:
#     print("Computer wins!")
# elif move == 0 and computer_move == 2:
#     print(name + " wins!")
# elif move == 1 and computer_move == 0:
#     print(name + " wins!")
# elif move == 1 and computer_move == 2:
#     print(name + " wins!")
# elif move == 2 and computer_move == 0:
#     print("Computer wins!")
# elif move == 2 and computer_move == 1:
#     print(name + " wins!")

import random

game_images = [rock, paper, scissors]

user_choice = int(input("What do you chose? Type ) for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer choose:")
    print(game_images[computer_choice])
    
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice  == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice < computer_choice:
        print("You lose!")
    elif user_choice == computer_choice:
        print("It's a tie!")