import random

def play_hangman():
  # List of words to choose from
  words = ["apple", "banana", "orange", "strawberry"]
  
  # Choose a random word
  word = random.choice(words)
  
  # Set up variables for the game
  word_letters = set(word)
  alphabet = set("abcdefghijklmnopqrstuvwxyz")
  used_letters = set()
  tries = 6
  
  # Main game loop
  while len(word_letters) > 0 and tries > 0:
    # Print the current game state
    print("Current word: " + get_word_display(word, used_letters))
    print("Tries remaining: " + str(tries))
    print("Used letters: " + " ".join(used_letters))
    
    # Get the player's next guess
    guess = input("Please enter a letter: ").lower()
    
    # Make sure the guess is valid
    if guess in alphabet - used_letters:
      used_letters.add(guess)
      if guess in word_letters:
        word_letters.remove(guess)
      else:
        tries -= 1
    else:
      print("Invalid guess. Please try again.")
      
  # Print the final result of the game
  if tries == 0:
    print("You lost! The word was " + word)
  else:
    print("Congratulations! You won! The word was " + word)
    
# Helper function to get the word display for the current game state
def get_word_display(word, used_letters):
  display = ""
  for letter in word:
    if letter in used_letters:
      display += letter
    else:
      display += "_"
  return display

# Start the game
play_hangman()
