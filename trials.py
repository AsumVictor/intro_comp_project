import time
def countdown(t): 
    for i in range(t+1):
        loading_bar = '⏰' * (t-i) + "_ " *i 
        progress = t-i
        print(f"\r{loading_bar} {progress:.1f}seconds ", end='', flush=False)
        time.sleep(1)
    print("")
    print("Time's up❗")


        
countdown(7)