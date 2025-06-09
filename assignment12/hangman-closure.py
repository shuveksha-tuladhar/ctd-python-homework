# Task 4: Closure Practice

def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter.lower())
        display = "".join(x if x in guesses else '_' for x in secret_word)
        print("Word:", display)
        return set(secret_word).issubset(guesses)
    return hangman_closure

if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").lower()
    print("\n" * 50)  
    print("Let's play Hangman!")

    game = make_hangman(secret_word)

    while True:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.")
            continue

        if game(guess):
            print(f"Congratulations! You guessed the word: {secret_word}")
            break
