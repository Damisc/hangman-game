import random
from hangman_words import word_list


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_game = False
lives = 6 

from art import logo
print(logo)

display = []
for _ in range(word_length):
    display += "_"


while not end_game:
    guess = input("Guess a letter in the word: ").lower()
    if guess in display:
        print(f"You already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter 
            

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word, You loose a life.")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You loose")


    print(f"{' '.join(display)}") 
    
    if "_" not in display:
        end_game = True
        print("You win.")


    from art import stages
    print(stages[lives])