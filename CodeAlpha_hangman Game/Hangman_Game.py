import random

# List of predefined words
words = ["python", "Java", "SQL", "C++", "javascript"]

# Choose a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("world of Hangman!")

while wrong_guesses < max_wrong:
    
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("wrong guesses left:", max_wrong - wrong_guesses)

    # Check if the player has guessed the word
    if "_" not in display_word:
        print("Congratulations! You guessed the word,you are genius:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Correct!")
    else:
        wrong_guesses += 1
        print(" Wrong guess!")

# If player runs out of guesses
if wrong_guesses == max_wrong:
    print("\n you are dead")
    print("The word was:", word)