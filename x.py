from inputimeout import inputimeout 
  
# Try block of code 
# and handle errors 
try: 
  
    # Take timed input using inputimeout() function 
    time_over = inputimeout(prompt='Name your best friend:', timeout=7)
    print(time_over) 
# Catch the timeout error 
except Exception: 
  
    # Declare the timeout statement 
    time_over = 'Your time is over!'
    print(time_over) 
  