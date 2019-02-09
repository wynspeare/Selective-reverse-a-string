import re

def reverse_string(string):
    word_array = list(string)
    word_to_reverse = []
    for index, char in enumerate(word_array):
        if char.isalnum():
            word_to_reverse.append(char)
            word_array[index] = " "
    for index, element in enumerate(word_array):
        if element == " ":
            word_array[index] = word_to_reverse[-1]
            word_to_reverse.pop()
    print(word_array)
    print(''.join(word_array))

reverse_string("!!aPples_Ar3__Gr8!")

def reverse_string_regex(string):
    word_array = list(string)
    word_to_reverse = []
    for index, char in enumerate(word_array):
        if re.search(r'[a-zA-Z0-9]', char):
            word_to_reverse.append(char)
            word_array[index] = " "
    for index, element in enumerate(word_array):
        if element == " ":
            word_array[index] = word_to_reverse[-1]
            word_to_reverse.pop()
    print(''.join(word_array))

reverse_string_regex("!!aPples_Ar3__Gr8!")

#Have a function that takes in a string
    # Create WORD_ARRAY from string
    # Create REVERSED_WORD empty array
    #Loop thru WORD_ARRAY to access each CHAR
        # If the CHAR is a LETTER or NUMBER
            # Add to WORD_TO_REVERSE    "aPplesAr3Gr8"
            # shift the CHAR onto beginning of REVERSED_WORD  "8rG3rAselpPa"
            #Replace CHAR with " "      ["!", "!", " ", " ", " ", " ", ]
    # Loop thru WORD_ARRAY 
        # If ELEMENT is " "
            # replace " " with WORD_TO_REVERSE's last element
            # Remove last element of WORD_TO_REVERSE
    # return joined WORD_ARRAY