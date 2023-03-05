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
import random

print("Welcome to Rock paper Scissors game")
game = [rock, paper, scissors]

num = int(
    input(
        'What do you choose? Type 0 or Rock, 1 for Paper, 2 for scissors:\n'))
if num >= 3 or num < 0:
    print("It's invalid number, you lose")
else:
  print("You chose")
  you_chose = game[num]
  print(you_chose)
  print('\n')

  computer_num = random.randint(0, (len(game) - 1))
  computer_chose = game[computer_num]
  print("computer chose")
  print(computer_chose)


  if num == computer_num:
    print("It's a draw")
# elif (num == 0 and computer_num == 1) or (num == 1 and computer_num == 2) or (num == 2 and computer_num == 1):
  elif (num == 0 and computer_num == 1) or (num == 1 and computer_num == 2) or (num == 2 and computer_num == 0):
    print("You lose")
  else:
    print("You win")