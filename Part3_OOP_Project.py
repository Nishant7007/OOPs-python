#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you and the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

mycards=[(s,r) for s in SUITE for r in RANKS]
#print(mycards)

class Deck:
    
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    
    
    def __init__(self):
        self.cards=mycards
        
    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.cards)
        
    def split_deck(self):
        print("SPLITTING CARDS")
        return (self.cards[:26],self.cards[26:])    
    


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards=cards
        
    def __str__(self):
        return "contains {} cards\n".format(len(self.cards))
    
    def add(self,added_cards):
        self.cards.extend(added_cards)
        
    def remove(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand
        print("welcome {}".format(name))
        
    def play_card(self):
        drawn_card=self.hand.remove()
        print("{} has placed {} \n".format(self.name,self.hand))
        return drawn_card
    
    def remove_war_cards(self):
        war_cards=[]
        if(len(self.hand.cards)<3):
            return self.hand.cards
        else:
            for i in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards
            
    
    def still_has_cards(self):
        """
        print true if still has cards
        """
        return len(self.hand.cards) !=0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
 
#create a new deck and split it into half

deck=Deck()
deck.shuffle()
half1,half2=deck.split_deck()

comp=Player('Computer',Hand(half1))

name=input("what is your name?")

player=Player(name,Hand(half2))


total_rounds=0
war_count=0

while(player.still_has_cards() & comp.still_has_cards()):
    total_rounds+=1
    print("Time for new round!\n")
    print("Here are the new standings\n")
    print("{} has the count: {}\n".format(player.name,len(player.hand.cards)))
    print("{} has the count: {}\n".format(comp.name,len(comp.hand.cards)))
    print("play a card!\n")
    
    table_cards=[]
    
    c_card=comp.play_card()
    p_card=player.play_card()
    
    table_cards.append(c_card)
    table_cards.append(p_card)
    print(c_card)
    
    if(c_card[1]==p_card[1]):
        war_count+=1
        
        print("war!\n")
        
        table_cards.extend(player.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())
        
        
        if(RANKS.index(c_card[1]) < RANKS.index(p_card[1])):
            player.hand.add(table_cards)
            
        else:
            comp.hand.add(table_cards)
            
        
    else:
        
        if(RANKS.index(c_card[1]) < RANKS.index(p_card[1])):
            player.hand.add(table_cards)
            
        else:
            comp.hand.add(table_cards)    
            

            
print("GAME OVER|\n")
print("Number of rounds: {}".format(total_rounds))
print("Number of war counts:{}".format(war_count))
if(len(player.hand.cards)<len(comp.hand.cards)):
    print("{} has won the game".format(comp.name))
else:
    print("{} has won the game".format(player.name))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        















