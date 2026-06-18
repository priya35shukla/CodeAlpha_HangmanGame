import random

# List of 5 predefined words
words = ["python", "computer", "program", "student", "science"]

# Select a random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman Game!")

while incorrect_guesses < max_incorrect:
    # Display the word with guessed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# If player loses
if incorrect_guesses == max_incorrect:
    print("\nGame Over!")
    print("The word was:", word)