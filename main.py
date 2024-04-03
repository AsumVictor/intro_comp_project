#Importing all utilized functions 
from helperFunctions import get_int, loader,  clear_screen, delay
from players import get_player_emoji, init_score_board, print_score_board, players

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
    prompt_message = """
    Press: 
    1 to Continue 
          or 
    any number to exit
    """
    user_choice = get_int(prompt_message)
    if user_choice != 1:
        print('You have Exited the game! Thank you😔')
        return
    
# Accept number of players (num_of_players)
    while True:
     num_of_players = get_int('How many players? ')
     if  num_of_players== 2 or  num_of_players == 3:
         break
     print('Number of players should be 2 or 3')
 
# Create account for all players
    for i in range(num_of_players):
        player_name = input(f"Type player {i + 1}'s name:  ")
        players.append({
            'name': player_name,
            'image': get_player_emoji()
        })
        
    
# initialized scoreboard -> 0
    score_board = init_score_board()
    print_score_board(score_board)
    
# Various Rounds

# Final score board

# Winner podium

    
    

main()