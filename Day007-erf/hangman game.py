import random
import os, subprocess
import hangman_words, hangman_art
chosen_word = random.choice(hangman_words.word_list) # gerefane kalame random az word_list
input("\n\t\twelcome to Hangman game, \n press any to continue...")
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
  letter_guessed = []
  
  blanked_word = blank_maker(chosen_word) # a List

  # game base
  while lives > 0:
    clear_screen()
    print(f"******************<{lives}/6 LEFT>***********************")
    print(f"the word is: {''.join(blanked_word)}")
    print(hangman_art.stages[lives])
    guess = input("guess a char:  ").lower()
    if guess in letter_guessed:
      input(f"you've guessed '{guess}' before , guess another letter")
      continue
    elif guess not in chosen_word: # ghalat hads zade
      lives -= 1
      input(f"the '{guess}' is wrong")
    if '_' not in blank_filler():
      break
    letter_guessed.append(guess)
    print(blank_filler())


  clear_screen()
  if lives == 0:
      print(f"******************< - - LOSE - - >***********************\nYou lose! the man just executed! \n {hangman_art.stages[0]}\nthe '{guess}' was wrong word was --> {chosen_word}\n  << << GAME OVER >> >>")
      input(f"")
  elif '_' not in blank_filler():
      print(f"******************< - - WON - - >***********************\nYou WON! your guess was correct --> {chosen_word} \n {hangman_art.stages[lives]}\n  << << WIN WIN >> >>")    
  



while True: # make program repeatable 
  print("___________________________________________________________\n")
  main()
  if input("\n Would you like to restart? (y/n)").lower() != 'y':
    break

