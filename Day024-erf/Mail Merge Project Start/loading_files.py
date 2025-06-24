
class LoadInput:
    def __init__(self):
        pass

    def names(self):
        """return a list of names, read from 'invited_names.txt'"""
        with open("./Input/Names/invited_names.txt", mode='r') as f:
            names = f.readlines()
        i=0
        for name in names:
            names[i] = name.replace('\n', '')
            i += 1
        return names

    def basic_letter(self):
        """return a string of basic letter read from 'starting_letter.txt'"""
        with open("./Input/Letters/starting_letter.txt", mode='r') as f:
            basic_letter = f.read()
        return basic_letter

