# Group 4 Unessay Project
# Authors: Sahil Brar, Roshan Shankar, Abel Tekeste, Maria Martine Baclig
# Password Hacking/Guessing Game wiht useful hints and techniques taught in class

import msvcrt

def startGame():
    EASY = "easy"
    HARD = "hard"
    print("`````` Welcome to Password Hacker *CHANGE NAME HERE* ``````")
    gameMode = input("Please select game difficulty, type either 'easy' or 'hard': ")

    for i in range(0, 100):
        if gameMode != EASY or gameMode != HARD:
            gameMode = input("Please select game difficulty, type either 'easy' or 'hard': ")

        if gameMode == EASY or gameMode == HARD:
            break
        
    
    if gameMode == EASY:
        playEasy()
    else:
        playHard()

# --- EASY MODE --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def playEasy():

    print("\n*** EASY MODE ***")

    # One of 4 easy mode profiles, must make a system to randomly pick, we can add more hints and stuff as needed
    PROFILE = "Ryan Henry"
    PASSWORD = "shredder"
    HINT = "Ryan's dog was named after a popular Teenage Mutant Ninja Turtles villain"
    
    display_pass = PASSWORD
    for j in range(0, len(display_pass)):                                                                                                        # length of password to be displayed
                display_pass = list(display_pass)                                                                                                # Change the password to a list (can't change strings in python)
                display_pass[j] = "*"                                                                                                            # Replace the letter to be hidden
                display_pass = "".join(display_pass)                                                                                             # Change list back into string
    
    for i in range(1, 11):                                                                                                                       # i is number of attempts (10) we can change this
        print("\nUser:    ", PROFILE,"\nHint:     ", HINT, "\nPassword:   ", display_pass, "\nAttempt:      ", i, "/10")                         # Output formatting for terminal
        guess = input("Enter your guess: ")

        for rannum in range(0, 100):                                                                                                             # Checking guess entered is the same length as password to be guessed
            if len(guess) != len(PASSWORD):
                print("\nPlease enter your guess of ", len(PASSWORD), " characters: ")
                guess = input("Enter your guess: ")

            if len(guess) == len(PASSWORD):
                break

        for j in range(0, len(PASSWORD)):                                                                                                        # length of password to check each char and change for output
            if guess[j] == PASSWORD[j]:                                                                                                          # Check each char, if the same then replace
                display_pass = list(display_pass)                                                                                                # Change the password to a list (can't change strings in python)
                display_pass[j] = guess[j]                                                                                                       # Replace the corresponding char
                display_pass = "".join(display_pass)                                                                                             # Change list back into string
        
        if guess == PASSWORD:
            print("\n*** User has been hacked successfully ***")
            print("User:    ", PROFILE,"\nPassword:   ", display_pass, "\nAttempt:      ", i, "/10")
            i = 100
        
        if i>11:
            break
    print("\nEnd of game\n")

# --- HARD MODE ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def playHard():
    print("\n*** HARD MODE ***")

    PROFILE = "Kate Upton"
    PASSWORD =  "C00kieMonst3r"
    HINT = "Seseme Street character loves cookies. Some letters may be numbers."

    display_pass = PASSWORD
    for j in range(0, len(display_pass)):                                                                                                        # length of password to be displayed
                display_pass = list(display_pass)                                                                                                # Change the password to a list (can't change strings in python)
                display_pass[j] = "*"                                                                                                            # Replace the letter to be hidden
                display_pass = "".join(display_pass)                                                                                             # Change list back into string

    for i in range(1, 11):                                                                                                                       # i is number of attempts (10) we can change this
        print("\nUser:    ", PROFILE,"\nHint:     ", HINT, "\nPassword:   ", display_pass, "\nAttempt:      ", i, "/10")                         # Output formatting for terminal
        guess = input("Enter your guess: ")

        for rannum in range(0, 100):                                                                                                             # Checking guess entered is the same length as password to be guessed
            if len(guess) != len(PASSWORD):
                print("\nPlease enter your guess of ", len(PASSWORD), " characters: ")
                guess = input("Enter your guess: ")

            if len(guess) == len(PASSWORD):
                break

        for j in range(0, len(PASSWORD)):                                                                                                        # length of password to check each char and change for output
            if guess[j] == PASSWORD[j]:                                                                                                          # Check each char, if the same then replace
                display_pass = list(display_pass)                                                                                                # Change the password to a list (can't change strings in python)
                display_pass[j] = guess[j]                                                                                                       # Replace the corresponding char
                display_pass = "".join(display_pass)                                                                                             # Change list back into string
        
        if guess == PASSWORD:
            print("\n*** User has been hacked successfully ***")
            print("User:    ", PROFILE,"\nPassword:   ", display_pass, "\nAttempt:      ", i, "/10")
            i = 100
        
        if i>11:
            break

# --- MAIN -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    startGame()
    #input("\nreached end of script. Hit enter to close.\n")
main()