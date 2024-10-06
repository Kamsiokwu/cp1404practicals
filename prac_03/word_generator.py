import random
import string

# Constants for vowels and consonants
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def generate_word(word_format):
    word = ""
    for kind in word_format:
        if kind == "c":  #consonant
            word += random.choice(CONSONANTS)
        elif kind == "v":  #vowel
            word += random.choice(VOWELS)
        elif kind.isalpha():  #other letters
            word += kind
    return word

user_format = input("Enter a word format (thus 'c' for consonants, 'v' for vowels, and any letters as is): ")
user_format = user_format.lower()

generated_word = generate_word(user_format)
print(f"Generated word: {generated_word}")
