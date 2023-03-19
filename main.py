import random
from hangman_word import word_list 
from hangman_stages import stages

print("Welcome to my very first Game (｡◕‿‿◕｡)")
print('''
 _   _   ____   __  _  ____  __  __   ____   __  _ 
| |_| | / () \ |  \| |/ (_,`|  \/  | / () \ |  \| |
|_| |_|/__/\__\|_|\__|\____)|_|\/|_|/__/\__\|_|\__|

''')
print("Below are the divisions that denote the length of the word")
print("So try and beat me  (̿▀̿‿ ̿▀̿ ̿) ")
# TODO1 randomly choose a word from the word_list and
# assign it to a varriable called chosen_word.
chosen_word = random.choice(word_list)
len_of_word = len(chosen_word)


empty_block= []
for block in range(len_of_word):
    empty_block+="_"
print(f"{'  '.join(empty_block)}")

# live variable
live = 6

# print([*chosen_word])
# TODO2 ask the user to guess a letter and assign their answer to a varriable
# called guess. make a guess lowercase
end_of_game = False
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
# TODO3 - Check if the letter the user guessed(guess)
# is one of the leters in the chosen_word
    counter = 0
    for letter in chosen_word:
        if guess == letter:
            empty_block[counter] = guess
        counter+=1
    # you have 6 live until u lose.
    if guess not in chosen_word:
        print(f"\nYou guessed {guess}, that's not in the word. You Lose a life.")
        live-=1
        if live == 0:
            end_of_game = True
            print("You Lose.")
    print(f"{'  '.join(empty_block)}")

    # win check.
    if "_" not in empty_block:
        end_of_game = True
        print("You Win!")
    print(stages[live])
# FINISH