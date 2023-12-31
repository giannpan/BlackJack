from random import randint
import time
cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suites = ['Hearts','Diamonds','Clubs','Spades']
values = {'A':11,
          'A1':1,
          '2':2,
          '3':3,
          '4':4,
          '5':5,
          '6':6,
          '7':7,
          '8':8,
          '9':9,
          '10':10,
          'J':10,
          'Q':10,
          'K':10}

Bank = 5000


print(f'Your bank is {Bank}')
playerplay = True
dealerplay = True
sp = False

def deal(ph,dh,dk):
    ph.append(dk.pop(randint(0,len(dk)-1)))
    dh.append(dk.pop(randint(0,len(dk)-1)))
    ph.append(dk.pop(randint(0,len(dk)-1)))
    dh.append('?')

def phands (dh,ph):
    if sp == False:
        print(f'\nDealer Hand: {dh}')
        print(f'Player Hand: {ph}\n')
        print(50*"*")
    else:
        print(f'\nDealer Hand: {dh}\n')
        print(f'Player Hand 1: {ph[0]}')
        print(f'Player Hand 2: {ph[1]}\n')
        print(50*"*")


def hit(hand,dk):
    if hand[1] == '?':
        hand[1] = dk.pop(randint(0,len(dk)-1))
        lst = list(map(lambda x: x[0],hand))
        if lst.count('A')>1:
            hand[lst.index('A')][0]='A1'
        q = sum(list(map(lambda x: values[x[0]],hand)))
        phands(dealerhand,playerhand)
    else:
        hand.append(dk.pop(randint(0,len(dk)-1)))
        lst = list(map(lambda x: x[0],hand))
        if lst.count('A')>1:
            hand[lst.index('A')][0]='A1'
        q = sum(list(map(lambda x: values[x[0]],hand)))
        phands(dealerhand,playerhand)
    return q

    
bet = int(input('Place your bet: '))    
playerhand = []
dealerhand = []
deck=[[i,j] for i in cards for j in suites]
deal(playerhand,dealerhand,deck)
phands(dealerhand,playerhand)


# Case when the player has BlackJack
if 'A' in [playerhand[0][0],playerhand[1][0]] and any(i in [playerhand[0][0],playerhand[1][0]] for i in ['10','J', 'Q','K']):
    print('BlackJack')
    bet *= 1,5
    dealerplay = False
    playerplay = False

# Case when the player can split
if playerhand[0][0] == playerhand[1][0]:
    z = input('Hit, Stand, Double or Split? ')
    if z == 'H':
        while z == 'H':
            m = hit(playerhand,deck)
            if m < 21:
                z = input('Hit or Stand? ')
            else:
                print('Player lose')
                dealerplay = False
                bet = -bet
                break
    elif z == 'SP':
        sp = True
        playerplay = False
        temp1 = [playerhand[0],deck.pop(randint(0,len(deck)-1))]
        temp2 = [playerhand[1],deck.pop(randint(0,len(deck)-1))]
        playerhand[0] = list(temp1)
        playerhand[1] = list(temp2)
        phands(dealerhand,playerhand)
        for i in range(len(playerhand)):
            z = input('Hit, Stand or Double? ')
            if z == 'H':
                while z == 'H':
                    m = hit(playerhand[i],deck)
                    if m <= 21:
                        z = input('Hit or Stand? ')
                    else:
                        print('Player lose')
                        playerhand[i] = '--'
                        bet = -bet
                        break
            elif z == 'D':
                # Double the bet
                m = hit(playerhand,deck)
            else:
                pass                        
    elif z == 'D':
        bet *= 2
        playerhand.append(deck.pop(randint(0,len(deck))))
        phands(dealerhand,playerhand)
    else:
        pass

# All other cases    
if playerhand[0][0] != playerhand[1][0] and playerplay:
    z = input('Hit, Stand or Double? ')
    if z == 'H':
        while z == 'H':
            m = hit(playerhand,deck)
            if m <= 21:
                z = input('Hit or Stand? ')
            else:
                print('Player lose')
                dealerplay = False
                bet = -bet
                break
    elif z == 'D':
        bet *= 2
        m = hit(playerhand,deck)
    else:
        pass



if dealerplay:
    k = hit(dealerhand,deck)
    # Dealers hand
    while k<17:
        time.sleep(2)
        k = hit(dealerhand,deck)
    
    if sp == False:
        m = sum(list(map(lambda x: values[x[0]],playerhand)))
        if k>m:
            bet = -bet
        elif k==m:
            bet = 0
        else:
            pass
    else:
        m1 = sum(list(map(lambda x: values[x[0]],playerhand[0])))
        m2 = sum(list(map(lambda x: values[x[0]],playerhand[1])))
        if k>m1:
            tbet1 = -bet
        elif k==m:
            tbet1 = 0
        else:
            tbet1 = bet
        if k>m2:
            tbet2 = -bet
        elif k==m:
            tbet2 = 0
        else:
            tbet2 = bet
        bet = tbet1 + tbet2

Bank += bet
