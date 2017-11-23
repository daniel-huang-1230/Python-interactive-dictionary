import json
from difflib import SequenceMatcher, get_close_matches


# first we load the json file and convert it to a python dict object

data = json.load(open('data.json'))



def translate(word):
    word = word.lower() #make it case insensitive first
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        return "Did you mean %s instead?" %get_close_matches(word,data.keys())[0]   #return the most similar match in the matches list
    else:
        return "The word doesn't exist. Please double check again"

word = input("Enter the word you want to look up for: ")
print(translate(word))