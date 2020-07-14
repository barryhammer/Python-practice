import json
from difflib import get_close_matches

def translate(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        # If there are more than 1 close matches to user entered input, ask if user meant most probable word.
        yn = list(input("Did you mean %s instead? Enter Y for yes, N for no: " % get_close_matches(w, data.keys())[0]))
        if yn[0].lower() == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn[0].lower() != 'n':
            return "Please try again using Y or N."
        else:
            return "The word is not in the dictionary."
    else:
        return "The word is not in the dictionary."

with open('data.json') as json_file:
    data = json.load(json_file)

    word = input("Enter a word: ").lower()
    output = translate(word)

    if type(output) == list: # Checks if return value is a list or a string message, iterates only by list from json file
        for item in output:
            print(item)
    else:
        print(output)