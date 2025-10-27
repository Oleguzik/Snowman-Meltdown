import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print("Word:", display_word)
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}\n")

def play_game():
    while True:
        secret_word = get_random_word()
        mistakes = 0
        guessed_letters = set()
        max_mistakes = len(STAGES) - 1
        print("\n==============================")
        print("Welcome to Snowman Meltdown!")
        print("==============================\n")
        while True:
            display_game_state(mistakes, secret_word, guessed_letters)
            guess = input("Guess a letter: ").strip().lower()
            if not guess or len(guess) != 1 or not guess.isalpha():
                print("[!] Please enter a single alphabetical letter.\n")
                continue
            if guess in guessed_letters:
                print("[!] You already guessed that letter.\n")
                continue
            guessed_letters.add(guess)
            if guess in secret_word:
                print("[✓] Good guess!\n")
            else:
                print("[✗] Wrong guess!\n")
                mistakes += 1
            if all(letter in guessed_letters for letter in secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print("🎉 Congratulations! You saved the snowman! 🎉\n")
                break
            if mistakes >= max_mistakes:
                display_game_state(mistakes, secret_word, guessed_letters)
                print(f"💀 Game over! The word was '{secret_word}'. The snowman melted. 💀\n")
                break
        replay = input("Would you like to play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing Snowman Meltdown!")
            break
