student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for index, row in data.iterrows()}

user_word = input("Enter a word: ")
user_word_letters = list(user_word.upper())
phonetic_alphabet = [nato_alphabet_dict[letter] for letter in user_word_letters if letter in nato_alphabet_dict]
print(phonetic_alphabet)



