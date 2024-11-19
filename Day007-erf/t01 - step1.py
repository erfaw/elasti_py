# todo 1,2,3
import random

word_list = ["aardvark", "baboon", "camel", "erfan", "asghar", "akbar"]
chosen_word = random.choice(word_list) # gerefane kalame random az word_list
shots = 11 # our HP actually :)
  

def main(): # MAIN 
  
  
  def blank_maker(word): # a func baraye sakhtane blank ha bar asas kalame vorodi ke random entekhab shde az ghabl
    blank_var =[]
    for x in word:
      blank_var.append('_')
    return blank_var
  
  
  blanked_word = blank_maker(chosen_word)
  print(chosen_word)
  print(''.join(blanked_word))

  guess = input("guess a char:\n").lower()
  for index, char in enumerate(chosen_word):
    if guess == char:
      print("yeaaaaah! right")
      blanked_word[index] = guess
  print(''.join(blanked_word))







while True: # make program repeatable 
  print("___________________________________________________________\n")
  main()
  if input("\nrestart? (y/n)").lower() != 'y':
    break

