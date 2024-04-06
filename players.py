# import random in-build function
import random

# Store players in a list of dictionary with keys, name and image
players = []

# A function to select random image for each player
def get_player_emoji():
    list_of_images = ['|👽|' ,'|💀|','|🐰|','|👶|','|🤶|','|🥷 |','|🤖|','|👹|']
    chosen_image = random.choice(list_of_images)
    chosen_image_index = list_of_images.index(chosen_image)
    # Delete image after choosing to avoid repeating same image
    del list_of_images[chosen_image_index]
    return chosen_image


# Function to initialized score board with players' score 0
def init_score_board():
    score_board = {}
    for player in players:
        name = player['image'] + ' ' + player['name']
        score_board[name] = 0

    return score_board

# A function to print the score board in a table board
# It accept the current scoreboard as an argument
def print_score_board(score_board):
    print("{:<25} {:<8} ".format('Player', 'Score'))
    print("{:<25} {:<8} ".format('------', '-----'))
    for name, score in score_board.items():
        print("{:<25} {:<8}".format(name, score))


