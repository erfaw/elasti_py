import pandas as pd
import subprocess; subprocess.call('cls', shell=True)

#DONE 1. Create a dictionary in this format:
nato_db = pd.read_csv("./Day026-erf/NATO-alphabet-start/nato_phonetic_alphabet.csv")
formated_dictionary_nato = {row.letter: row.code for (index, row) in nato_db.iterrows()}

#DONE 2. Create a list of the phonetic code words from a word that the user inputs.
def check_input():
    global user_word 
    u_w = input('Please enter your name or message:\n')
    try:
        for letter in u_w:
            formated_dictionary_nato[letter.upper()]
    except KeyError:
        print("sorry, input corr!!!#############X")
        check_input()
    else:
        user_word = u_w
    
# user_word = input('Please enter your name or message:\n') 
check_input() 
user_word_splited_list = list(user_word)

print(user_word_splited_list)
nato_for_user = [formated_dictionary_nato[f_char.upper()] for f_char in user_word_splited_list]
print(nato_for_user)