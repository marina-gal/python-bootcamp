
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

game_images = [rock,paper,scissors]

# My choice
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if my_choice >= 0 and my_choice <=2:
    print(game_images[my_choice])

# Computer's choice
computer_choice= random.randint(0,2)
print(f"Computer chose {game_images[computer_choice]}")


# Setting the conditions
if my_choice >= 3 or my_choice < 0:
    print("You typed an invalid number. You lose! ") # Choosing only valid numbers
elif my_choice == 0 and computer_choice == 2:
    print("You win") # setting the exceptions
elif computer_choice > my_choice:
    print("You loose") # setting the rule1
elif my_choice == computer_choice:
    print("It's a draw! ")
elif computer_choice == 0 and my_choice == 2:
    print("You loose") # setting the exceptions
elif my_choice > computer_choice:
    print("You win! ")  # setting the rule1
