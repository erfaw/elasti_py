#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
import os; os.system('cls')
from loading_files import LoadInput

load = LoadInput()

names = load.names()
basic_letter = load.basic_letter()

basic_letter = basic_letter.replace('[name]', 'erfan')
print(basic_letter)
print(names)