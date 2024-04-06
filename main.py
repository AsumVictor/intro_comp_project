# Importing all utilized functions
from helperFunctions import get_int, loader,  clear_screen, delay
from players import get_player_emoji, init_score_board, print_score_board, players
from rounds import go_to_round
from questionBank import mathematics_set_1, mathematics_set_2,general_knowledge_set_1, general_knowledge_set_2, Computing_set_1, Computing_set_2, science_set_1, science_set_2


def main():
    # Initial loading screen for game
    loader("Vicel Trivia Quiz Game🤓")

# Print something in screen press something contine
    print("""Welcome to Vicel Trivia Quiz 🧠 Game!
     💡 🧮 🖥️ 🧪""")
    delay(1.25)
    clear_screen()
# Game Rules
    print(""" Game Rules
    1.There are only 2-3 players🫂
    2. There are 4 rounds in the game:
    General Knowledge💡, Math🧮, Computing 🖥️ and Science🧪
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
    clear_screen()
    while True:
        num_of_players = get_int('How many players👥? ')
        if num_of_players == 2 or num_of_players == 3:
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
    go_to_round(round_number=1, round_category="General Knowlege", round_emoji="💡",
           round_questions_set1=general_knowledge_set_1, round_questions_set2=general_knowledge_set_2, score_board=score_board)
    print_score_board(score_board)
    
    go_to_round(round_number=2, round_category="Mathematics", round_emoji="🧮",
           round_questions_set1=mathematics_set_1, round_questions_set2=mathematics_set_2, score_board=score_board)
    print_score_board(score_board)
    
    go_to_round(round_number=3, round_category="Computing", round_emoji="🖥️",
           round_questions_set1=Computing_set_1, round_questions_set2=Computing_set_2, score_board=score_board)
    print_score_board(score_board)

    go_to_round(round_number=4, round_category="Science", round_emoji="🧪",
           round_questions_set1=science_set_1, round_questions_set2=science_set_2, score_board=score_board)
    print_score_board(score_board)

# Final score board

# Winner podium


main()
