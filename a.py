import random

def number_guessing_game():
    print("Welcome to number guessing game !")
    target_number = random.randint(1, 100)  
    right_to_guess = 7  

    while right_to_guess > 0:
        try:
            guess = int(input("Please make a guess (between 1-100): "))
            if 1 <= guess <= 100:
                if guess == target_number:
                    print(f"Congratulations! Right guess, target number {target_number}.")
                    break
                elif guess < target_number:
                    print("Enter a higher number please.")
                else:
                    print("Enter a lower number please.")
                right_to_guess -= 1
            else:
                print("İnvalid login. Please enter a number between 1-100.")
        except ValueError:
            print("İnvalid login. Please enter a integer number.")
        
        
        if right_to_guess == 0:
            print(f"You are out of quesses. Target number was {target_number}.")


number_guessing_game()
