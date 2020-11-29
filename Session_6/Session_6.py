# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:04:52 2020

@author: Mutum
"""

import random

# 1 Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck - 50 pts

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

n = []
t = list(map(lambda y: list(map(lambda x: n.append((y, x)), vals)), suits))
print(n)


# 2 Write a normal function without using lambda, zip, and map function to create 52 cards in a deck - 50 pts

# TODO: Impement Function
# Function to create all 52 card in a game of cards 
def normal_func(vals:'A list of 13 value of a suit of a card',
                suits:'A list of the four suits') -> 'A list of 52 card of the four suits':
    
    ''' 
    
    Creates 52 different cards from 4 suits each of 13 values
    Cuation : This functions did not use ambda, zip, and map function
    
    Inputs:
        vals : the 13 different values of a suits
        suits : the four suits 
    return :
        the 52 different card from all suits
    '''
    if len(suits) !=4:
        raise ValueError("Yoh we have only 4 suits !!")
    if len(vals) !=13:
        raise ValueError("Yoh ever suits has 13 cards !")
        
    result = []
    for sui in suits:
        for val in vals:
            result.append((sui,val))
    return result

normal_func(vals,suits)

# Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with
# each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify 
# who won the game of poker (Links to an external site.)! - 150 pts

# TODO: Impement Function
# Function to decide who wins in a game of cars by two players
def play_card(players: 'int: No. of players',
                cards_num : 'int: No. of cards drawn in a play',
                deck : 'A list of 52 playing card'):    
    '''
    For any two player which can pull card 3/4/5 each in a play, this functions calculates which players
    wins the game !
    
    - For winning below are the ranking , 1 or "Royal Flush" being the highest rank. Whoever ranks higher wins the game 
    - If both the player`s card does not falls under the 10 category/ranking, winner is decided base on the 
    total values of the card    
    
    Category or ranking:
    category_mapping = {1:"Royal Flush",2:"Straight Flush",3:"Four of a kind",
                        4:"Full House",5:"Flush",6:"Straight",7:"Three of a kind",
                        8:"Two pair",9:"One Pair",10:"High Card"}
    
    weightage for each card values if both player cards does not fall in above ranking
    value_mapping = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9, 
                     'jack':10, 'queen':11, 'king':12, 'ace':13}
    
    Inputs:
        players : No. of player - Integer value. This functioins consider only 2 players
        cards_num: No. of card to be drawn by each player in a play
        deck: The 52 cards - A list
    Return:
        Winner of the game!!
    '''
    
    value_mapping = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9, 
                     'jack':10, 'queen':11, 'king':12, 'ace':13}
    
    category_mapping = {1:"Royal Flush",2:"Straight Flush",3:"Four of a kind",
                        4:"Full House",5:"Flush",6:"Straight",7:"Three of a kind",
                        8:"Two pair",9:"One Pair",10:"High Card"}
    
    if players !=2:
        raise ValueError("Only two players are allower- supply 2 as integer")
    if cards_num not in [3,4,5]:
        raise ValueError("ONly 3/4/5 cards allowed in play - supply as integer value")
    if len(deck) !=52:
        raise ValueError("Yoh ever play card !!, total 52 cards in a play !")
        
    player_1 = None
    player_2 = None
    
    if players==2 and cards_num in [3,4,5] and len(deck)==52:
        player_1 = random.sample(deck,cards_num)
        player_2 = random.sample(deck,cards_num)

    else:
        if players !=2:
            raise ValueError("Only 2 players are allowed !!")
        if cards_num not in [3,4,5]:
            raise ValueError("Each players are allowed only 3,4 or 5 cards in one play")
        if len(deck)!=52:
            raise ValueError("A deck should have 52 cards !")
    #return {"player_1":player_1,"player_2":player_2} 
    #print(result.extend(player_1))
    
    # player`s card ranking
    
    player_1 = sorted(player_1,key = lambda x : x)
    
    suits_player_1 = [card[0] for card in player_1]
    suits_player_2 = [card[0] for card in player_2]
    
    vals_player_1 = [card[1] for card in player_1]
    vals_player_2 = [card[1] for card in player_2]
    
    #print(suits_player_1)
    # print(vals_player_1)
    
    # print(suits_player_2)
    # print(vals_player_2)
    
    rank_player_1 = None
    rank_player_2 = None
          
    if cards_num == 5 and rank_player_1 is None:
        
        if len(set(suits_player_1))==1 and 'ace' in vals_player_1 and 'king' in vals_player_1 \
            and 'queen' in vals_player_1 and 'jack' in vals_player_1 and '10' in vals_player_1 :
            rank_player_1 = 1  # Royal Flush
            
        elif len(set(suits_player_1))==1 and '10' in vals_player_1 and '9' in vals_player_1 \
            and '8' in vals_player_1 and '7' in vals_player_1 and '6' in vals_player_1:
            rank_player_1 = 2 # Straight Flush
            
        elif len(set(suits_player_1))==1 and 'king' in vals_player_1  and '8' in vals_player_1 and '6' in vals_player_1 \
            and '4' in vals_player_1 and '2' in vals_player_1:
            rank_player_1 = 5 # Flush
        elif max([vals_player_1.count(val) for val in set(vals_player_1)]) == 4 :
            rank_player_1 = 3 # Four of a kind
        elif max([vals_player_1.count(val) for val in set(vals_player_1)]) == 3 :
            rank_player_1 = 7 # Three of a kind
        elif len(set(vals_player_1))== 2 and 'king' in vals_player_1  and 'ace' in vals_player_1  and vals_player_1.count("ace")==3:
            rank_player_1 = 4 # Full house
        elif len(set(suits_player_1))==4 and [vals_player_1.count(val) for val in set(vals_player_1)].count(2) == 2 :
            rank_player_1 = 8 # Two pair
        elif len(set(suits_player_1))==4 and [vals_player_1.count(val) for val in set(vals_player_1)].count(2) == 1 :
            rank_player_1 = 9 # One pair
        elif len(set(suits_player_1))==4 and len(set(vals_player_1))==5 and 'ace' in vals_player_1 and 'queen' in vals_player_1 :
            rank_player_1 = 10 # High Card - contains ace and queen rest card are unique
        elif len(set(suits_player_1))==4 and len(set(vals_player_1))==5 and ("ace" not in vals_player_1) and ("king" not in vals_player_1) and ("queen" not in vals_player_1) and ('jack' not in vals_player_1) and ( int(min(vals_player_1)) + 4 == int(max(vals_player_1)) ):
            rank_player_1 = 6 # straight  , all numbers in series
        else:
            rank_player_1 = 0 #"No category"   
            
            # ranking player 2 starts
    if cards_num == 5 and rank_player_2 is None :
                          
        if len(set(suits_player_2))==1 and 'ace' in vals_player_2 and 'king' in vals_player_2 \
            and 'queen' in vals_player_2 and 'jack' in vals_player_2 and '10' in vals_player_2 :
            rank_player_2 = 1  # Royal Flush
            
        elif len(set(suits_player_2))==1 and '10' in vals_player_2 and '9' in vals_player_2 \
            and '8' in vals_player_2 and '7' in vals_player_2 and '6' in vals_player_2:
            rank_player_2 = 2 # Straight Flush
            
        elif len(set(suits_player_2))==1 and 'king' in vals_player_2 and '8' in vals_player_2 \
            and '6' in vals_player_2 and '4' in vals_player_2 and '2' in vals_player_2:
            rank_player_2 = 5 # Flush
        elif max([vals_player_2.count(val) for val in set(vals_player_2)]) == 4 :
            rank_player_2 = 3 # Four of a kind
        elif max([vals_player_2.count(val) for val in set(vals_player_2)]) == 3 :
            rank_player_2 = 7 # Three of a kind
        elif len(set(vals_player_2))== 2 and 'king' in vals_player_2 and 'ace' in vals_player_2  \
            and vals_player_2.count("ace")==3:
            rank_player_2 = 4 # Full house
        elif len(set(suits_player_2))==4 and [vals_player_2.count(val) for val in set(vals_player_2)].count(2) == 2 :
            rank_player_2 = 8 # Two pair
        elif len(set(suits_player_2))==4 and [vals_player_2.count(val) for val in set(vals_player_2)].count(2) == 1 :
            rank_player_2 = 9 # One pair
        elif len(set(suits_player_2))==4 and len(set(vals_player_2))==5 and 'ace' in vals_player_2 \
            and 'queen' in vals_player_2 :
            rank_player_2 = 10 # High Card - contains ace and queen rest card are unique
        elif len(set(suits_player_2))==4 and len(set(vals_player_2))==5 and ("ace" not in vals_player_2) and ("king" not in vals_player_2) and ("queen" not in vals_player_2) and ('jack' not in vals_player_2) and ( int(min(vals_player_2)) + 4 == int(max(vals_player_2)) ):
            rank_player_2 = 6 # straight  , all numbers in series
       
        else:
            rank_player_2 = 0 # "No category"

    if cards_num == 4 and rank_player_1 is None :
                       
        if len(set(suits_player_1))==1 and 'ace' in vals_player_1 and 'king' in vals_player_1 \
            and 'queen' in vals_player_1 and 'jack' in vals_player_1 :
            rank_player_1 = 1  # Royal Flush
            
        elif len(set(suits_player_1))==1 and '10' in vals_player_1 and '9' in vals_player_1 \
            and '8' in vals_player_1 and '7' in vals_player_1 :
            rank_player_1 = 2 # Straight Flush
            
        elif len(set(suits_player_1))==1 and 'king' in vals_player_1  and '8' in vals_player_1 and '6' in vals_player_1 \
            and '4' in vals_player_1 :
            rank_player_1 = 5 # Flush
        elif max([vals_player_1.count(val) for val in set(vals_player_1)]) == 4 :
            rank_player_1 = 3 # Four of a kind
        elif max([vals_player_1.count(val) for val in set(vals_player_1)]) == 3 :
            rank_player_1 = 7 # Three of a kind
        elif len(set(vals_player_1))== 2 and 'king' in vals_player_1  and 'ace' in vals_player_1  and vals_player_1.count("ace")==3:
            rank_player_1 = 4 # Full house
        elif len(set(suits_player_1))==4 and [vals_player_1.count(val) for val in set(vals_player_1)].count(2) == 2 :
            rank_player_1 = 8 # Two pair
        elif len(set(suits_player_1))==4 and [vals_player_1.count(val) for val in set(vals_player_1)].count(2) == 1 :
            rank_player_1 = 9 # One pair
        elif len(set(suits_player_1))==4 and len(set(vals_player_1))==4 and 'ace' in vals_player_1 and 'queen' in vals_player_1 :
            rank_player_1 = 10 # High Card - contains ace and queen rest card are unique
        elif len(set(suits_player_1))==4 and len(set(vals_player_1))==4 and ("ace" not in vals_player_1) and ("king" not in vals_player_1) and ("queen" not in vals_player_1) and ('jack' not in vals_player_1) and ( int(min(vals_player_1)) + 3 == int(max(vals_player_1)) ):
            rank_player_1 = 6 # straight  , all numbers in series
        else:
            rank_player_1 = 0 #"No category"
           
            # ranking player 2 starts
    if cards_num == 4 and rank_player_2 is None :
                                 
        if len(set(suits_player_2))==1 and 'ace' in vals_player_2 and 'king' in vals_player_2 \
            and 'queen' in vals_player_2 and 'jack' in vals_player_2 :
            rank_player_2 = 1  # Royal Flush
            
        elif len(set(suits_player_2))==1 and '10' in vals_player_2 and '9' in vals_player_2 \
            and '8' in vals_player_2 and '7' in vals_player_2 :
            rank_player_2 = 2 # Straight Flush
            
        elif len(set(suits_player_2))==1 and 'king' in vals_player_2  and '8' in vals_player_2 and '6' in vals_player_2 \
            and '4' in vals_player_2 :
            rank_player_2 = 5 # Flush
        elif max([vals_player_2.count(val) for val in set(vals_player_2)]) == 4 :
            rank_player_2 = 3 # Four of a kind
        elif max([vals_player_2.count(val) for val in set(vals_player_2)]) == 3 :
            rank_player_2 = 7 # Three of a kind
        elif len(set(vals_player_2))== 2 and 'king' in vals_player_2  and 'ace' in vals_player_2  and vals_player_2.count("ace")==3:
            rank_player_2 = 4 # Full house
        elif len(set(suits_player_2))==4 and [vals_player_2.count(val) for val in set(vals_player_2)].count(2) == 2 :
            rank_player_2 = 8 # Two pair
        elif len(set(suits_player_2))==4 and [vals_player_2.count(val) for val in set(vals_player_2)].count(2) == 1 :
            rank_player_2 = 9 # One pair
        elif len(set(suits_player_2))==4 and len(set(vals_player_2))==4 and 'ace' in vals_player_2 and 'queen' in vals_player_2 :
            rank_player_2 = 10 # High Card - contains ace and queen rest card are unique
        elif len(set(suits_player_2))==4 and len(set(vals_player_2))==4 and ("ace" not in vals_player_2) and ("king" not in vals_player_2) and ("queen" not in vals_player_2) and ('jack' not in vals_player_2) and ( int(min(vals_player_2)) + 3 == int(max(vals_player_2)) ):
            rank_player_2 = 6 # straight  , all numbers in series
        else:
            rank_player_2 = 0 #"No category"

    if cards_num == 3 and rank_player_1 is None :
                       
        if len(set(suits_player_1))==1 and 'ace' in vals_player_1 and 'king' in vals_player_1 \
            and 'queen' in vals_player_1 :
            rank_player_1 = 1  # Royal Flush
            
        elif len(set(suits_player_1))==1 and '10' in vals_player_1 and '9' in vals_player_1 \
            and '8' in vals_player_1:
            rank_player_1 = 2 # Straight Flush
            
        elif len(set(suits_player_1))==1 and 'king' in vals_player_1  and '8' in vals_player_1 and '6' in vals_player_1 :
            rank_player_1 = 5 # Flush
            
        # elif max([vals_player_1.count(val) for val in set(vals_player_1)]) == 4 :
        #     rank_player_1 = 3 # Four of a kind
        
        elif max([vals_player_1.count(val) for val in set(vals_player_1)]) == 3 :
            rank_player_1 = 7 # Three of a kind
        elif len(set(vals_player_1))== 1  and 'ace' in vals_player_1 :
            rank_player_1 = 4 # Full house
        elif len(set(suits_player_1))==3 and [vals_player_1.count(val) for val in set(vals_player_1)].count(2) == 2 :
            rank_player_1 = 8 # Two pair
        elif len(set(suits_player_1))==3 and [vals_player_1.count(val) for val in set(vals_player_1)].count(2) == 1 :
            rank_player_1 = 9 # One pair
        elif len(set(suits_player_1))==3 and len(set(vals_player_1))==3 and 'ace' in vals_player_1 and 'queen' in vals_player_1 :
            rank_player_1 = 10 # High Card - contains ace and queen rest card are unique
        elif len(set(suits_player_1))==3 and len(set(vals_player_1))==3 and ("ace" not in vals_player_1) and ("king" not in vals_player_1) and ("queen" not in vals_player_1) and ('jack' not in vals_player_1) and ( int(min(vals_player_1)) + 2 == int(max(vals_player_1)) ):
            rank_player_1 = 6 # straight  , all numbers in series
        else:
            rank_player_1 = 0 #"No category"
           
            # ranking player 2 starts
    if cards_num == 3 and rank_player_2 is None :
                                 
        if len(set(suits_player_2))==1 and 'ace' in vals_player_2 and 'king' in vals_player_2 \
            and 'queen' in vals_player_2 :
            rank_player_2 = 1  # Royal Flush
            
        elif len(set(suits_player_2))==1 and '10' in vals_player_2 and '9' in vals_player_2 \
            and '8' in vals_player_2 :
            rank_player_2 = 2 # Straight Flush
            
        elif len(set(suits_player_2))==1 and 'king' in vals_player_2  and '8' in vals_player_2 and '6' in vals_player_2 :
            rank_player_2 = 5 # Flush
            
        # elif max([vals_player_2.count(val) for val in set(vals_player_2)]) == 4 :
        #     rank_player_2 = 3 # Four of a kind
        
        elif max([vals_player_2.count(val) for val in set(vals_player_2)]) == 3 :
            rank_player_2 = 7 # Three of a kind
        elif len(set(vals_player_2))== 1 and 'ace' in vals_player_2:
            rank_player_2 = 4 # Full house
        elif len(set(suits_player_2))==3 and [vals_player_2.count(val) for val in set(vals_player_2)].count(2) == 2 :
            rank_player_2 = 8 # Two pair
        elif len(set(suits_player_2))==3 and [vals_player_2.count(val) for val in set(vals_player_2)].count(2) == 1 :
            rank_player_2 = 9 # One pair
        elif len(set(suits_player_2))==3 and len(set(vals_player_2))==3 and 'ace' in vals_player_2 and 'queen' in vals_player_2 :
            rank_player_2 = 10 # High Card - contains ace and queen rest card are unique
        elif len(set(suits_player_2))==3 and len(set(vals_player_2))==3 and ("ace" not in vals_player_2) and ("king" not in vals_player_2) and ("queen" not in vals_player_2) and ('jack' not in vals_player_2) and ( int(min(vals_player_2)) + 2 == int(max(vals_player_2)) ):
            rank_player_2 = 6 # straight  , all numbers in series
        else:
            rank_player_2 = 0 #"No category"
            
    #print(rank_player_1)
    #print(rank_player_2)
       
    
    # if rank_player_1 == rank_player_2 !=0:
    #     return "Hard luck - Draw !!"
    if rank_player_2 > rank_player_1 and rank_player_1 != 0:
        return "Player_1 wins !!!"
    elif rank_player_1 > rank_player_2 and rank_player_2 != 0:
        return "Player_2 wins !!!"
    elif rank_player_2 > rank_player_1 and rank_player_1 == 0:
        return "Player_2 wins !!!"
    elif rank_player_1 > rank_player_2 and rank_player_2 == 0:
        return "Player_1 wins !!!"
    else:
        sum_player_1 = sum([value_mapping[x] for x in vals_player_1])
        sum_player_2 = sum([value_mapping[x] for x in vals_player_2])
        if sum_player_1 > sum_player_2:
            return "Player_1 wins !!!"
        else:
            return "Player_2 wins !!!"
                 
# play_card(2,4,n)
   
# [_[0] for _ in [('clubs', 'ace'), ('hearts', '4'), ('diamonds', 'ace')]]

# for _ in [('clubs', 'ace'), ('hearts', '4'), ('diamonds', 'ace')]:
#     print(_[0])

# dummy_playr = [('hearts', '6'), ('diamonds', '7'), ('spades', '7')]
# dummy_vals = [card[1] for card in dummy_playr]
# dummy_vals
# [dummy_vals.count(val) for val in set(dummy_vals)]
# max([dummy_vals.count(val) for val in dummy_vals])

# for i in range(1000):
#     print(play_card(2,5,n))

