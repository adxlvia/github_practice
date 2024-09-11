import random

# List of 5-letter words (you can expand this list as needed)
WORD_LIST = ["apple", "grape", "peach", "mango", "berry"]

def get_random_word():
    return random.choice(WORD_LIST)

def display_feedback(guess, secret_word):
    feedback = ['_'] * len(guess)
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            feedback[i] = guess[i].upper()  # Correct letter in the correct position
        elif guess[i] in secret_word:
            feedback[i] = guess[i].lower()  # Correct letter but wrong position
    return " ".join(feedback)

def wordle():
    secret_word = get_random_word()
    attempts = 6
    print("Welcome to Wordle!")
    print("Guess the 5-letter word. You have 6 attempts.")

    while attempts > 0:
        guess = input("Enter your guess: ").strip().lower()

        if len(guess) != 5 or not guess.isalpha():
            print("Invalid input. Please enter a 5-letter word.")
            continue
        
        if guess == secret_word:
            print(f"Congratulations! You've guessed the word: {secret_word.upper()}")
            break

        feedback = display_feedback(guess, secret_word)
        print(f"Feedback: {feedback}")
        attempts -= 1
        print(f"Attempts remaining: {attempts}")
    
    if guess != secret_word:
        print(f"Sorry, you've run out of attempts. The word was: {secret_word.upper()}")

if __name__ == "__main__":
    wordle()