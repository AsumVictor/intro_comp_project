import time
import os

def get_int(message):
    # Confirm user integer input 
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

def loader(message, emoji='🎮'): 
    clear_screen() 
    print(message)
    for i in range(11):
        loading_bar = emoji *i + '.' * (10-i)
        progress = i/10 * 100
        print(f"\r{loading_bar} {progress:.1f}%", end='')
        time.sleep(0.2)

    clear_screen()

def clear_screen():
    # clear console screen
    os.system('cls')

def delay(s):
    time.sleep(s)

def countdown(t): 
    for i in range(t+1):
        loading_bar = '⏰' * (t-i) + "_ " *i 
        progress = t-i
        print(f"\r{loading_bar} {progress:.1f}seconds ", end='', flush=False)
        time.sleep(1)
    print("")
    print("Begin❗")

