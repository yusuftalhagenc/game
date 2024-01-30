# game
import random: This imports the random module, which is used to generate a random number later in the code.

def number_guessing_game():: This line defines a function called number_guessing_game.

print("Welcome to number guessing game !"): This prints a welcome message to the user when the game starts.

target_number = random.randint(1, 100): This line generates a random integer between 1 and 100 (inclusive) and assigns it to the variable target_number. This is the number that the player needs to guess.

right_to_guess = 7: This initializes the variable right_to_guess to 7, representing the number of guesses the player has.

The code enters a while loop, which continues as long as right_to_guess is greater than 0.

Inside the loop, the player is prompted to enter a guess using input("Please make a guess (between 1-100): ").

The entered guess is converted to an integer using int(), and then the code checks whether the guess is within the valid range (between 1 and 100).

If the guess is within the valid range, the code compares it with the target_number. Depending on the comparison, the player is informed whether to guess higher or lower, and the right_to_guess counter is decremented.

If the guess is equal to the target_number, the player is congratulated, and the game breaks out of the loop.

If the guess is not within the valid range, an error message is displayed, and the player is prompted to enter a valid number.

If a ValueError occurs (e.g., if the user enters a non-integer), an error message is displayed, and the player is prompted to enter a valid integer.

If the player runs out of guesses (right_to_guess == 0), the game informs the player that they are out of guesses and reveals the correct target number.

The number_guessing_game() function is called at the end, initiating the game.








