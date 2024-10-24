import random

word_list = ["aardvark", "baboon", "camel"]

# TO-DO 1 - Randomly choose a word from word_list
chosen_word = random.choice(word_list)
print(chosen_word)

#TO Do 2 - Ask the user to guess a letter
guess = input("Insert your guess here : ").lower()

# TO DO 3 - Check if the letter the user guessed is on the chosen word_list
for letter in chosen_word :
    if guess == letter:
        print("Correct")
    else:
        print("Wrong")

