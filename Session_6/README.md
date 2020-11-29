# Epai_Session_6


## Single line expression
- 1 Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck - 50 pts

Here we use lambda and map functions to create 52 different card of a game
```
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

n = []
t = list(map(lambda y: list(map(lambda x: n.append((y, x)), vals)), suits))

```
- Initialise empty list
- Run for loop twice to collect the cards as tuple in the empty list

### Functions definition
- 2 normal_func : Write a normal function without using lambda, zip, and map function to create 52 cards in a deck

This functions did the same thing as above single expression but write as a normal function

- Annotation and Docstrings are added for better documentation

```
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

```
### Functions definition
-3 Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game of cards

This functions prints who wins the game between two player
This decision for winning is written in the Docstring
```

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

  ```

  ### Note a series of test (pytest) are executed using githubs actions
