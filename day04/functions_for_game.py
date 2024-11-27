from pynput import keyboard
import random

# Defining global variables to control game flow
game_running = True
new_game = False
secret_num = None  # Initialize secret_num as a global variable

def on_press(key):
    global game_running, new_game, secret_num
    try:
        if key.char == 'x':
            print("Exiting the game")
            game_running = False
            return False  # Stop the listener
        elif key.char == 'n':
            print("Starting a new game...")
            new_game = True    
            return False #return False
        elif key.char == 's':
            print(f"The hidden number is {secret_num}, you cheater!")
            return False  # Stop the listener
    except AttributeError:
        pass

def play_game():
    global game_running, new_game, secret_num
    game_running = True
    new_game = False
    while game_running:
        secret_num = random.randint(1, 20)  # The computer "thinks" about a whole number between 1 and 20.
        print(secret_num)
        
        if not game_core(secret_num):
            print("Goodbye")
            break
        if new_game:
            new_game = False  # Reset the flag for the next game

def game_core(secret_num):
    global game_running, new_game
    
    listener = keyboard.Listener(on_press=on_press)  # Creating the listener in the function.
    listener.start()  # Starting the listener.
        
    guess_counter = 1  # Initiation of a counter of the guessing trials.
    
    users_guess = int(input("Guess a whole number between 1-20: ")) 
    
    while game_running and not new_game:
        if users_guess < secret_num:
            print("Your guess is too small!")
            users_guess = int(input("Guess a larger number: "))
            guess_counter += 1
        elif users_guess > secret_num:
            print("Your guess is too big!")
            users_guess = int(input("Guess a smaller number: "))        
            guess_counter += 1     
        else:
            if guess_counter == 1:
                print("Great guess, made it on your first try!")
            else:
                print(f"That's right! It took you {guess_counter} tries.")
            break  # Exit the loop when the correct guess is made

        if new_game == True:
            break

    listener.stop()
    if new_game:
        return True
    
    # At the end of the game, we ask the user if they want to start a new game:
    response = input("Do you want to start a new game? (yes/no) ").lower()
    if response == "yes":
        new_game = True
        return True
    else:
        game_running = False
        return False