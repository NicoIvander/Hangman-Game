import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in chosen_word :
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""
    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(correct_letter)
    print(display)

    if "_" not in display:
        game_over = True
        print("You Win!")

