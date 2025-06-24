#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

# open invited_names.txt for catch names in a list first
with open("g:/myDocuments/Programming/Python/elasti_py/Day024-erf/Mail Merge Project Start/Input/Names/invited_names.txt", mode='r') as f:
    names = f.readlines()

i=0
for name in names:
    names[i] = name.replace('\n', '')
    i += 1

