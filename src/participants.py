import random

def process_names(namesstring):
    names = namesstring.split(',')
    names = [name.strip() for name in names]
    if len(names) < 4 or len(names) > 7:
        raise ValueError("Must have 4-7 participants.")    
    if len(set(names)) != len(names):
        raise ValueError("Duplicate names are not allowed.")
    if "" in names:
        raise ValueError("Empty names are not allowed.")
    return names
    
def prompt_participants():
    while True:
        namesstring = input(("Please enter the names of 4-7 participants and separate them by comma: "))
        try:
            names = process_names(namesstring)
            random.shuffle(names)
            return names
        except ValueError as e:
            print(f"Invalid input: {e}")