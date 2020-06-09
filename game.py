# Group 4 Unessay Project
# Authors: Sahil Brar, Roshan Shankar, Abel Tekeste, Maria Martine Baclig
# Password Hacking/Guessing Game wiht useful hints and techniques taught in class
import random
from tkinter import *
root = Tk()
root.geometry("500x250")
HINT = ""

# --- EASY MODE --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def easyMode():
    for ele in root.winfo_children():
        ele.destroy()
    title = Label(root, text="EASY MODE").pack()

    # Randomly select which user to hack
    choice = random.randint(1,4)
    if choice == 1:
        PROFILE = "Ryan Henry"
        PASSWORD = "shredder"
        HINT = "Ryan's dog was named after a popular Teenage Mutant Ninja Turtles villain"   

    if choice == 2:
        PROFILE = "Mr. Chow"
        PASSWORD = "123456" 
        HINT = "Most used password in the world"

    if choice == 3:
        PROFILE = "Alan Turing"
        PASSWORD = "honey"
        HINT = "Winnie the pooh favorite food"

    if choice == 4:
        PROFILE = "Scarlett"
        PASSWORD = "paris" 
        HINT = "Love capital of the world"

    profileLabel = Label(root, text= "Profile: "+PROFILE).pack()
    
    display_pass = PASSWORD
    # length of PASSWORD to be displayed
    for j in range(0, len(display_pass)):
        # Change the PASSWORD to a list (can't change strings in python)
        display_pass = list(display_pass)
        # Replace the letter to be hidden
        display_pass[j] = "*"
        # Change list back into string
        display_pass = "".join(display_pass)

    passwordLabel = Label(root, text = "Password: "+ display_pass).pack()
    hintLabel = Label(root, text = "Hint: "+HINT).pack()
    guessLabel = Entry().pack()

    # i is number of attempts (10) we can change this
    for i in range(1, 11):
        print("\nUser:    ", PROFILE, "\nHint:     ", HINT, "\nPassword:   ", display_pass,
              "\nAttempt:      ", i, "/10")                         # Output formatting for terminal
        guess = Label(root, text="whats your guess")
        # Checking guess entered is the same length as PASSWORD to be guessed
        for rannum in range(0, 100):
            if len(guess) != len(PASSWORD):
                print("\nPlease enter your guess of ",
                      len(PASSWORD), " characters: ")
                guess = Label(root, text="whats your guess")
                if len(guess) == len(PASSWORD):
                    break

        # length of PASSWORD to check each char and change for output
        for j in range(0, len(PASSWORD)):
            # Check each char, if the same then replace
            if guess[j] == PASSWORD[j]:
                # Change the PASSWORD to a list (can't change strings in python)
                display_pass = list(display_pass)
                # Replace the corresponding char
                display_pass[j] = guess[j]
                # Change list back into string
                display_pass = "".join(display_pass)

        if guess == PASSWORD:
            print("\n*** User has been hacked successfully ***")
            print("User:    ", PROFILE, "\nPassword:   ",
                  display_pass, "\nAttempt:      ", i, "/10")
            print("\nEnd of game\n")
            break

# --- HARD MODE ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def hardMode():
    for ele in root.winfo_children():
        ele.destroy()
    title = Label(root, text="HARD MODE").pack()

    PROFILE = "Kate Upton"
    PASSWORD = "C00kieMonst3r"
    HINT = "Seseme Street character loves cookies. Some letters may be numbers."
    display_pass = PASSWORD

    # length of PASSWORD to be displayed
    for j in range(0, len(display_pass)):
        # Change the PASSWORD to a list (can't change strings in python)
        display_pass = list(display_pass)
        # Replace the letter to be hidden
        display_pass[j] = "*"
        # Change list back into string
        display_pass = "".join(display_pass)
    
    profileLabel = Label(root, text= "Profile: "+PROFILE).pack()
    passwordLabel = Label(root, text = "Password: "+ display_pass).pack()
    hintLabel = Label(root, text = "Hint: "+HINT).pack()
    guessLabel = Entry().pack()

    # i is number of attempts (10) we can change this
    for i in range(1, 11):
        print("\nUser:    ", PROFILE, "\nHint:     ", HINT, "\nPassword:   ", display_pass,
              "\nAttempt:      ", i, "/10")                         # Output formatting for terminal
        guess = Label(root, text="whats your guess")

        # Checking guess entered is the same length as PASSWORD to be guessed
        for rannum in range(0, 100):
            if len(guess) != len(PASSWORD):
                print("\nPlease enter your guess of ",
                      len(PASSWORD), " characters: ")
                guess = Label(root, text="whats your guess")

            if len(guess) == len(PASSWORD):
                break

        # length of PASSWORD to check each char and change for output
        for j in range(0, len(PASSWORD)):
            # Check each char, if the same then replace
            if guess[j] == PASSWORD[j]:
                # Change the PASSWORD to a list (can't change strings in python)
                display_pass = list(display_pass)
                # Replace the corresponding char
                display_pass[j] = guess[j]
                # Change list back into string
                display_pass = "".join(display_pass)

        if guess == PASSWORD:
            print("\n*** User has been hacked successfully ***")
            print("User:    ", PROFILE, "\nPassword:   ",
                  display_pass, "\nAttempt:      ", i, "/10")
            break


# --- START SCREEN ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    
EASY = "easy"
HARD = "hard"
welcome = Label(root, text="Welcome to the PASSWORD guessing game")
welcome.pack()
difficulty = Label(root, text= "please choose your difficulty")
easyButton = Button(root, text="EASY", fg="red", command = easyMode)
hardButton = Button(root, text="HARD", fg="red", command = hardMode)
difficulty.pack()
easyButton.pack()
hardButton.pack()


                
root.mainloop()
