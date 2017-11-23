import json
from difflib import SequenceMatcher, get_close_matches


# first we load the json file and convert it to a python dict object

data = json.load(open('data.json'))



def translate(word):

    word = word.lower() #make it case insensitive first
    if word in data:
        return data[word]
    elif word.title() in data:
        #title() will convert the first letter to
        # uppercase and the others to lowercase.
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0:
        userAns = input("Did you mean %s instead? Enter Y if yes, or N if no: " %get_close_matches(word,data.keys())[0])
        if userAns == 'Y' or 'y':
            # return the most similar match in the matches list
            return data[get_close_matches(word,data.keys())[0]]
        elif userAns == 'N' or 'n':
            return "The word doesn't exist. Please double check again."
        else:
            return "Sorry, we didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check again."

word = input("Enter the word you want to look up for: ")
output = translate(word)

#distinguish between the return type (str or list)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)