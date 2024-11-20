import random
import os
import subprocess


word_list = ["aardvark", "baboon", "camel", "erfan", "asghar", "akbar"]
chosen_word = random.choice(word_list) # gerefane kalame random az word_list

stages = [ # ascii arts
  r'''
    +-------+
    O       |
   /|\      |
   / \      |
            |
            |
    =========
''', #0 
  r'''
    +-------+
    O       |
   /|\      |
   /        |
            |
            |
    =========
''', #1
  r'''
    +-------+
    O       |
   /|\      |
            |
            |
            |
    =========
''', #2
  r'''
    +-------+
    O       |
   / \      |
            |
            |
            |
    =========
''', #3
  r'''
    +-------+
    O       |
   /        |
            |
            |
            |
    =========
''', #4
  r'''
    +-------+
    O       |
            |
            |
            |
            |
    =========
''', #5
  r'''
    +-------+
            |
            |
            |
            |
            |
    =========
''', #6
]

def main(): # MAIN 
  def blank_maker(word): # a func baraye sakhtane blank ha bar asas kalame vorodi ke random entekhab shde az ghabl
    blank_var =[]
    for x in word:
      blank_var.append('_')
    return blank_var
  
  def display_filled_maker(): # function baraye por kardan blank ha tebgh guess khode doore
    display_filled = ''
    for x in chosen_word:
      if guess == x:
        display_filled += guess
      else:
        display_filled += '_'
    return display_filled
  
  def blank_filler(): # funtion khodam baraye por kardan blank ha tebgh guess
    for index, char in enumerate(chosen_word):
      if guess == char:
        # print("yeaaaaah! right")
        blanked_word[index] = guess
    return ''.join(blanked_word)
  
  def clear_screen():
    # Use subprocess to call the appropriate command
    if os.name == 'nt':  # For Windows
        subprocess.call('cls', shell=True)
    else:  # For macOS and Linux
        subprocess.call('clear', shell=True)
  
  lives = 6 # our HP actually :)
  
  blanked_word = blank_maker(chosen_word) # a List

  while lives > 0:
    clear_screen()
    print(f"the word is: {''.join(blanked_word)}")
    print(stages[lives])
    guess = input("guess a char:  ").lower()
    
    if guess not in chosen_word: # ghalat hads zade
      lives -= 1
    
    print(blank_filler())
  clear_screen()
  if lives == 0:
      print(f"You lost! the man just executed! \n {stages[0]}\n\t GAME OVER")
  



while True: # make program repeatable 
  print("___________________________________________________________\n")
  main()
  if input("\nrestart? (y/n)").lower() != 'y':
    break

