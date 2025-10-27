import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Select a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the current ASCII art and the word with guessed letters."""
    print(STAGES[mistakes])
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print(f"Word: {display_word}")
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}\n")

def get_valid_guess(guessed_letters):
    """Prompt the user for a valid guess and return it."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("[!] Please enter a single alphabetical letter.\n")
            continue
        if guess in guessed_letters:
            print("[!] You already guessed that letter.\n")
            continue
        return guess

def ask_replay():
    """Ask the user if they want to play again."""
    while True:
        replay = input("Would you like to play again? (y/n): ").strip().lower()
        if replay in ("y", "n"):
            return replay == "y"
        print("Please enter 'y' or 'n'.")

def run_single_game():
    """Run a single game session."""
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = set()
    max_mistakes = len(STAGES) - 1
    print("\n==============================")
    print("Welcome to Snowman Meltdown!")
    print("==============================\n")
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = get_valid_guess(guessed_letters)
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

def play_game():
    """Main entry point for the game, handles replay loop."""
    while True:
        run_single_game()
        if not ask_replay():
            print("Thanks for playing Snowman Meltdown!")
            break
