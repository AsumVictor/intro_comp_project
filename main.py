#Importing all utilized functions 
from helperFunctions import get_int, loader,  clear_screen, delay
from players import get_player_emoji, init_score_board, print_score_board

def main():
#Initial loading screen for game 
    loader("Vicel Trivia Game🎲")

# Print something in screen press something contine
    print("""Welcome to Vicel Trivia Game!
     🧮 📜 🏭 🧪""")
    delay(1.25)
    clear_screen()       
#Game Rules
    print(""" Game Rules
    1.There are only 2-3 players🫂
    2. There are 4 rounds in the game:
    Math🧮, history📜,Engineering🏭 and Science🧪
    3. You have only 7 seconds to answer questions
              Good Luck!🤞
    """)
    ans = get_int(input(""" Press 
                        1 to continue 
                        or
                        2 to End if you are chicken 🐔😂"""))

# Accept number of players (num_of_players)
 
# Create account for all players

# initialized scoreboard -> 0

# Print Game rules 

# Various Rounds

# Final score board

# Winner podium

    
    

main()