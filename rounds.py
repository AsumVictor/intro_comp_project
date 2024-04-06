from helperFunctions import loader,  clear_screen, delay,countdown
from players import players
import random


def go_to_round(*,round_number,round_category,round_emoji, round_questions_set1, round_questions_set2, score_board):
    print(f'---- ROUND {round_number} ----')
    delay(1)
    loader(round_category, round_emoji)

    print('PROBLEM SET 1')
    countdown(3)

    delay(1)
    # two set for round one
    for player in players:
        clear_screen()
        name = player['image'] + ' ' + player['name']
        print(f"{name} your turn!")
        question, answer = get_question(round_questions_set1)
        print(question)
        print(' ')
        user_answer = input_validator('a-d')
        print(f"{user_answer} is ", end='')
        point = is_answer_correct(answer, user_answer, "others")

        score_board[name] += point
        
        delay(1.5)
        
    clear_screen()
    
    
    print('True or False Set')
    countdown(3)
    # two set for round one
    for player in players:
        clear_screen()
        name = player['image'] + ' ' + player['name']
        print(f"{name} your turn!")
        question, answer = get_question(round_questions_set2)
        print(question)
        print(' ')
        user_answer = input_validator('a-b')
        print(f"{user_answer} is ", end='')
        point = is_answer_correct(answer, user_answer, "others")
        if point == 3:
            score_board[name] += point
        else:
            score_board -= point

        delay(1.5)
    clear_screen()
    print(f"The results after the {round_category} round, the standings are:")
    countdown(3,"🥁", message=' ')
    print("   ____ SCORE BOARD _____ \n")
        
    
    
    # for every set we will ask each player different question with same standard

    #  Every set will have different time

    # multiprocessing
    # MCQ - 10 sec

    # T/F - 5 sec


def get_question(question):
    chosen_question = random.choice(list(question.keys()))
    answer = question[chosen_question]
    del question[chosen_question]
    return [chosen_question, answer]


def input_validator(range):
    allowed_val = {
        'a-d': ['a', 'b', 'c', 'd'],
        'a-b': ['a', 'b']
    }
    while True:
        try:
            user_input = input(f'Type your answer ({range}): ').lower().strip()
            if user_input == None:
                return None
            
            if not user_input in allowed_val[range]:
                raise ValueError

            return user_input
        except:
            print(f'Your answer must be {range} ')


def is_answer_correct(answer, player_answer, type):
    points = {
        't/f': [3, 1],
        'others': [5, 0]
    }

    if answer == player_answer:
        print("Correct ✅")
        return points[type][0]
    else:
        print("Wrong ❌")
        print(f"The correct answer is {answer}")
        return points[type][1]


