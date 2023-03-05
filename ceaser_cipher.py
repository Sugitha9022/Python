from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

is_input = True

# step 3
def ceaser_cipher(text_msg, shift_num, direction):
  ceaser_msg = ""
  if direction == "decode":
    shift_num *= -1
  for letter in text_msg:
    if letter in alphabet:
      pos = alphabet.index(letter)
      new_pos = pos + shift_num
      if new_pos > 25 or new_pos <0:
        new_pos %=26
      ceaser_msg += alphabet[new_pos]
    else:
      ceaser_msg += letter
  print(f"{direction}d message is {ceaser_msg}")




# step 1 - import logo
print(logo)

# step 2 - take inputs
while is_input:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser_cipher(text_msg=text, shift_num = shift, direction = direction)

    user_input = input("\nType yes if you wanna go again or else no:  ")
    if user_input == "yes":
      is_input = True
    else:
      is_input = False
      print("Goodbye\n")





