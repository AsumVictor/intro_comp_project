# Store All players info
import random
players = []


def get_player_emoji():
    list_of_images = ['|👽|' ,'|💀|','|🐰|','|👶|','|🤶|','|🥷 |','|🤖|','|👹|']
    chosen_image = random.choice(list_of_images)
    chosen_image_index = list_of_images.index(chosen_image)
    del list_of_images[chosen_image_index]
    return chosen_image



def init_score_board():
    score_board = {}
    for player in players:
        name = player['image'] + ' ' + player['name']
        score_board[name] = 0

    return score_board


def print_score_board(score_board):
    print("{:<25} {:<8} ".format('Player', 'Score'))
    print("{:<25} {:<8} ".format('------', '-----'))
    for name, score in score_board.items():
        print("{:<25} {:<8}".format(name, score))


