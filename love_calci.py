print("Welcome to Love calculator \n")
name1 = input("What's your name: ")
name2 = input("What's their name: ")

total_len = len(name1)+ len(name2)
name = name1.upper()+name2.upper()

count_true = 0
count_love = 0

for i in range(total_len):
  if name[i] in "TRUE":
    count_true += 1
  if name[i] in "LOVE":
    count_love += 1

Love_percent = int(str(count_true) + str(count_love))

# For Love Scores less than 10 or greater than 90, the message should be:
if Love_percent < 10 or Love_percent > 90:
  print(f"Your score is {Love_percent}, you go together like coke and mentos.")
#For Love Scores between 40 and 50, the message should be:
elif Love_percent > 40 and Love_percent < 50:
  print(f"Your score is {Love_percent}, you are alright together.")
else:
  print(f"Your score is {Love_percent}")