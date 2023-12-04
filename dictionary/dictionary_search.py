import json
with open('dictionary/dictionary.json', 'r') as dictionary_file:
    data = json.load(dictionary_file) 

# lets search for a key in the json file
def search_for_word(entered_word):
    if entered_word in data:
        print("word is present as a key")
        return True
    else: 
        print("word is not present as a key")
        print(f"Please enter a word from the list below: \n{data.keys()} ")
        return False
# lets get the value of a key
def get_value(word_definition):
    if word_definition == True:
        return data[entered_key]
    
# let's ask the user for a word
entered_key = input("enter a word to look for: \n")
word_definition = search_for_word(entered_key)

# lets print the data returned
print(f"The definition of {entered_key} is: {get_value(word_definition)}")