# Importing in built functions
import time
import os

#Creation of a funtion that filters user input to ensure that they are positive integers
def get_int(message): 
    while True: # try till input is a positive interger
        try:
            n = input(f'{message}: ')
            n = int(n)
            if n < 0:
                raise ValueError
            return n
        except:
            print()
            print('Please type in a positive integer to proceed!')

#Creation of a reusable function that displays a loading screen and message based on the set emoji and message passed as input
def loader(message, emoji='🎮'): 
    clear_screen() 
    print(message)
    for i in range(11):
        loading_bar = emoji *i + '.' * (10-i)
        progress = i/10 * 100
        print(f"\r{loading_bar} {progress:.1f}%", end='')
        time.sleep(0.2)

    clear_screen()

#Creation of a function that clears the terminal screen whenever called
def clear_screen():
    # clear console screens 
    # For linux and MacOS
    if(os.name == 'posix'):
      os.system('clear')
    # else screen will be cleared for windows
    else:
      os.system('cls')

#Creation of a function that casuses a delay or pause between different lines of code running
def delay(s):
    time.sleep(s)

#Creation of a function that loads a countdown interface in between rounds
def countdown(t, emoji='⏳', message ="Begin❗"): 
    for i in range(t+1):
        loading_bar = emoji * (t-i) + "_ " *i 
        progress = t-i
        print(f"\r{loading_bar} {progress:.1f}seconds ", end='', flush=False)
        time.sleep(1)
    print("")
    print(message)

