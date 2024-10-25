import random

word_list = ["aardvark", "baboon", "camel"]

# TO-DO 1 - Randomly choose a word from word_list
chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
for letter in chosen_word :
    placeholder += "_"
print(placeholder)
guess = input("Guess a letter: ").lower()


display = ""
for letter in chosen_word:
    if letter == guess:
        display += guess
    else:
        display += "_"

print(display)
