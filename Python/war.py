import random
from random import randint as rint

running = True

def shuffledDeck():
    basic_deck = list(range(2,15))*4
    print(basic_deck)
    random.shuffle(basic_deck)
    return basic_deck

deck = shuffledDeck()

player1 = input("Whats your name? \n")
player2 = input("Whats your name? \n")

shuffledDeck()

turn = 0

Points1 = 0
Points2 = 0

war = False

#Turn function
def player_turn():
        #Global lets functions use outside vars
        global war
        draw = deck.pop(0)
        
        if turn % 2 == 1:
            name = player1
            card1.append(draw)
            
        else:
            name = player2
            card2.append(draw)

        print(f"{name} drew card {draw}")
        print(card1)
        print(card2)
        return draw

card1 = []
card2 = []

def compare():
        global Points1
        global Points2
        global war

        if card1[0] > card2[0]:
            if war:
                #if war it gives more points
                print(f"{player1} Wins!")
                Points1 += 6
            else:
                print(f"{player1} Wins!")
                Points1 += 2
        elif card2[0] > card1[0]:
            if war:
                print(f"{player2} Wins!")
                Points2 += 6
            else:
                Points2 += 2
                print(f"{player2} Wins")
        else:
            print("A war is happening!")
            war = True

while running:

    print(turn)

    if turn > 1:
        if turn % 2 == 1:
            pass
        else:
            compare()
            card1 = []
            card2 = []

    if turn % 2 == 1:
        name = player1
    else:
        name = player2

    choice = input(f"Would you like to play {name}? y/n \n")
    if choice == 'y':
        player_turn()
    elif choice == 'n':
        running = False
        break
    else:
        print("That is not an option.")
        turn += 0
    
    if turn >= 51:
        print(f"Game has ended! \n{player1} has {Points1}. \n{player2} has {Points2}")
        if Points1 > Points2:
            print(f"{player1} wins with: {Points1}")
        elif Points2 > Points1:
            print(f"{player2} wins with {Points2}")
        else:
            print("Its a tie!")
        running = False
        break
    
    #Lonely ahh addition
    turn += 1