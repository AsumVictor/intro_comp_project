from helperFunctions import get_int, loader,  clear_screen, delay
from questionBank import mathematics_set_1, mathematics_set_2
from players import players,get_player_emoji
import random
from inputimeout import inputimeout 


for i in range(2):
        players.append({
            'name': 'player_name',
            'image': get_player_emoji()
        })

def round_1():
    print('---- ROUND 1 ----')
    delay(1)
    loader('     Mathematics','🧮') 
    
    print('PROBLEM SET 1')
    print('You have only 10 seconds in this set')
    delay(1)
    # two set for round one
    for player in players:
        clear_screen()
        name = player['image'] + ' ' + player['name']
        print(f"{name} your turn!")
        question, answer = get_question(mathematics_set_1)
        print(question)
        print(' ')
        user_answer = input_validator('a-d')
        print(f"{user_answer} is ", end='')
        point = is_answer_correct(answer,user_answer,"others")
        
        
        delay(3)
        
        
    
    # for every set we will ask each player different question with same standard
    
    #  Every set will have different time
    
    # MCQ - 10 sec
    
    # T/F - 5 sec
    
    


def get_question(question):
    chosen_question = random.choice(list(question.keys()))
    answer = question[chosen_question]
    del question[chosen_question]
    return [chosen_question, answer]


def input_validator(range):
    allowed_val = {
          'a-d': ['a','b','c','d'],
          'a-b':['a','b']
      }
    while True:
        try:
            user_input = input(f'Type your answer ({range}): ').lower().strip()
            
            if not user_input in allowed_val[range]:
                raise ValueError
            
            return user_input
        except:
            print(f'Your answer must be {range} ')
        

def is_answer_correct(answer, player_answer,type):
    points = {
        't/f': [3, -1],
        'others' : [5, 0]
    }
    
    if answer == player_answer:
       print("Correct ✅")
       return points[type][0]
    else:
     print("Wrong ❌")
     print(f"The correct answer is {answer}")
     return points[type][1]


round_1()