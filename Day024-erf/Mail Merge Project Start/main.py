#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
import os
os.system('cls')   

# open invited_names.txt for catch names in a list first
with open("./Input/Names/invited_names.txt", mode='r') as f:
    names = f.readlines()

i=0
for name in names:
    names[i] = name.replace('\n', '')
    i += 1

with open("./Input/Letters/starting_letter.txt", mode='r') as f:
    basic_letter = f.read()

basic_letter = basic_letter.replace('[name]', 'erfan')


print(basic_letter)