import random
import string

def choose_word():
    words = ["python", "fish", "developer", "hangman", "monkey"]
    return random.choice(words)
    
def get_guess():
    guess = input("Guess a letter: ").lower()
    while len(guess) != 1 or guess not in string.ascii_lowercase: 
        guess = input("Guess a letter: ").lower()
    return guess

def play_game():
    word = choose_word()
    complete_word = "_" * len(word)
    lives = 5

    print("Let's play Hangman!")
    print(complete_word)

    while lives > 0 and "_" in complete_word:
        print(f"Lives left: {lives}")
        guess = get_guess()
        
        if guess in word:
            complete_word = "".join(letter if letter == guess or letter in complete_word else "_" for letter in word)
            print(f"Good job! {complete_word}")
        else:
            lives -= 1
            print(f"{guess} is not in the word.")
   
    if "_" not in complete_word:
        print("Congrats, you guessed the word!")
    else:
        
        print(f"Sorry, you are out of lives. The word was '{word}'.")

def hangman():
    while True:
        play_game()
        restart = input("Would you like to play again? (yes/no): ").lower()
        if restart != "yes":
            print("Thanks for playing, come back soon!")
            break

if __name__ == "__main__":
    hangman()

        
