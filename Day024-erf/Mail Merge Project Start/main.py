import os; os.system('cls')
from loading_files import LoadInput

load = LoadInput()
names = load.names()
basic_letter = load.basic_letter()

for name in names:
    output_letter = basic_letter.replace('[name]', name)
    with open(f"./Output/ReadyToSend/{name}.txt", mode='w') as f:
        f.write(output_letter)
