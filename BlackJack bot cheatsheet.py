from random import randint
import time
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tqdm import tqdm

cheatsheet = {
5: ['H','H','H','H','H','H','H','H','H','H'],
6: ['H','H','H','H','H','H','H','H','H','H'],
7: ['H','H','H','H','H','H','H','H','H','H'],
8: ['H','H','H','H','H','H','H','H','H','H'],
9: ['H','D','D','D','D','H','H','H','H','H'],
10: ['D','D','D','D','D','D','D','D','H','H'],
11: ['D','D','D','D','D','D','D','D','D','D'],
12: ['H','H','S','S','S','H','H','H','H','H'],
13: ['S','S','S','S','S','H','H','H','H','H'],
14: ['S','S','S','S','S','H','H','H','H','H'],
15: ['S','S','S','S','S','H','H','H','H','H'],
16: ['S','S','S','S','S','H','H','H','H','H'],
17: ['S','S','S','S','S','S','S','S','S','S'],
18: ['S','S','S','S','S','S','S','S','S','S'],
19: ['S','S','S','S','S','S','S','S','S','S'],
20: ['S','S','S','S','S','S','S','S','S','S'],
21: ['S','S','S','S','S','S','S','S','S','S'],
'A,2': ['H','H','H','D','D','H','H','H','H','H'],
'A,3': ['H','H','H','D','D','H','H','H','H','H'],
'A,4': ['H','H','D','D','D','H','H','H','H','H'],
'A,5': ['H','H','D','D','D','H','H','H','H','H'],
'A,6': ['H','D','D','D','D','H','H','H','H','H'],
'A,7': ['S','D','D','D','D','S','S','H','H','H'],
'A,8': ['S','S','S','S','S','S','S','S','S','S'],
'A,9': ['S','S','S','S','S','S','S','S','S','S'],
'2,2': ['SP','SP','SP','SP','SP','SP','H','H','H','H'],
'3,3': ['SP','SP','SP','SP','SP','SP','H','H','H','H'],
'4,4': ['H','H','H','SP','SP','H','H','H','H','H'],
'5,5': ['D','D','D','D','D','D','D','D','H','H'],
'6,6': ['SP','SP','SP','SP','SP','H','H','H','H','H'],
'7,7': ['SP','SP','SP','SP','SP','SP','H','H','H','H'],
'8,8': ['SP','SP','SP','SP','SP','SP','SP','SP','SP','SP'],
'9,9': ['SP','SP','SP','SP','SP','S','SP','SP','S','S'],
'10,10': ['S','S','S','S','S','S','S','S','S','S'],
'J,J': ['S','S','S','S','S','S','S','S','S','S'],
'Q,Q': ['S','S','S','S','S','S','S','S','S','S'],
'K,K': ['S','S','S','S','S','S','S','S','S','S'],
'A,A': ['SP','SP','SP','SP','SP','SP','SP','SP','SP','SP']
}

columns = [2,3,4,5,6,7,8,9,10,'A']
df = pd.DataFrame(cheatsheet, index = columns).T
df

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

results = {'Wins' : [],
           'BlackJack': [],
           'Loses': [],
           'Draws': [],
           'P/L': []
            }
    
bankroll = []
        
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
#            phands(dealerhand,playerhand)
    else:
        hand.append(dk.pop(randint(0,len(dk)-1)))
        lst = list(map(lambda x: x[0],hand))
        if lst.count('A')>1:
            hand[lst.index('A')][0]='A1'
            q = sum(list(map(lambda x: values[x[0]],hand)))
#           phands(dealerhand,playerhand)
        else:
            qtemp = sum(list(map(lambda x: values[x[0]],hand)))
            if qtemp>21 and 'A' in lst:
                hand[lst.index('A')][0]='A1'
                q = sum(list(map(lambda x: values[x[0]],hand)))
#               phands(dealerhand,playerhand)
            else:
                q = sum(list(map(lambda x: values[x[0]],hand)))
#               phands(dealerhand,playerhand)
    return q
    
def choice (ph,dh):
    lsp = list(map(lambda x: x[0],ph))
    b = dh[0][0]
    if len(lsp)==2:
        if 'A' in lsp or lsp[0]==lsp[1]:
            a = ','.join(sorted(lsp,reverse = True))
        else:
            a = sum(list(map(lambda x: values[x],lsp)))
    else:
        a = sum(list(map(lambda x: values[x],lsp)))
    if b == 'A':
        pass
    else:
        b = values[b]        
    return df.loc[a,b]


for g in tqdm(range(10)):
    for v in results.values():v.append(0) 
    bnkrlist = []
    Bank = 5000
    for i in range (1000000):   
#        print(f'Your bank is {Bank}')
        playerplay = True
        dealerplay = True
        sp = False
        bet = 100
        playerhand = []
        dealerhand = []
        deck=[[i,j] for i in cards for j in suites]
        deal(playerhand,dealerhand,deck)
        #    phands(dealerhand,playerhand)

        # Case when the player has BlackJack
        if 'A' in [playerhand[0][0],playerhand[1][0]] and any(i in [playerhand[0][0],playerhand[1][0]] for i in ['10','J', 'Q','K']):
#            print('BlackJack')
            bet *= 1.5
            dealerplay = False
            playerplay = False
            results['BlackJack'][g] += 1

        # Case when the player can split
        if playerhand[0][0] == playerhand[1][0]:
            z = choice(playerhand,dealerhand)
            if z == 'H':
                while z == 'H':
                    m = hit(playerhand,deck)
                    if m < 21:
                        z = choice(playerhand,dealerhand)
                    else:
#                        print('Player lose')
                        dealerplay = False
                        bet = -bet
                        results['Loses'][g] += 1
#                        print('Dealer wins')
                        break
            elif z == 'SP':
                sp = True
                playerplay = False
                temp1 = [playerhand[0],deck.pop(randint(0,len(deck)-1))]
                temp2 = [playerhand[1],deck.pop(randint(0,len(deck)-1))]
                playerhand[0] = list(temp1)
                playerhand[1] = list(temp2)
#                phands(dealerhand,playerhand)
                for i in range(len(playerhand)):
                    if 'A' in [playerhand[i][0][0],playerhand[i][1][0]] and any(j in [playerhand[i][0][0],playerhand[i][1][0]] for j in ['10','J', 'Q','K']):
#                        print('BlackJack')
                        bet *= 1.5
                        results['BlackJack'][g] += 1
                        break
                    z = choice(playerhand[i],dealerhand)
                    if z == 'H':
                        while z == 'H':
                            m = hit(playerhand[i],deck)
                            if m <= 21:
                                z = choice(playerhand[i],dealerhand)
                            else:
                                #print('Player lose')
                                playerhand[i] = '--'
                                bet = -bet
                                results['Loses'][g] += 1
                                #print('Dealer wins')
                                break
                    elif z == 'D':
                        bet *= 2
                        m = hit(playerhand[i],deck)
                    else:
                        pass                        
            elif z == 'D':
                bet *= 2
                m = hit(playerhand,deck)
    #            phands(dealerhand,playerhand)
            else:
                pass
        
        # All other cases    
        if playerhand[0][0] != playerhand[1][0] and playerplay:
            z = choice(playerhand,dealerhand)
            if z == 'H':
                while z == 'H':
                    m = hit(playerhand,deck)
                    if m <= 21:
                        z = choice(playerhand,dealerhand)
                    else:
                        #print('Player lose')
                        dealerplay = False
                        bet = -bet
                        results['Loses'][g] += 1
                        #print('Dealer wins')
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
                k = hit(dealerhand,deck)
            
            if sp == False:
                m = sum(list(map(lambda x: values[x[0]],playerhand)))
                if k>m and k<=21:
                    bet = -bet
                    results['Loses'][g] += 1
                    #print('Dealer wins')
                elif k==m:
                    bet = 0
                    results['Draws'][g] += 1
                    #print('Draw')
                else:
                    results['Wins'][g] += 1
                    #print('Player wins')
            else:
                m1 = sum(list(map(lambda x: values[x[0]],playerhand[0]))) if playerhand[0]!=(['--', '--'] and '--') else 0
                m2 = sum(list(map(lambda x: values[x[0]],playerhand[1]))) if playerhand[1]!=(['--', '--'] and '--') else 0
                if k>m1 and k<=21:
                    tbet1 = -bet
                    results['Loses'][g] += 1
                    #print('Dealer wins')
                elif k==m1:
                    tbet1 = 0
                    results['Draws'][g] += 1
                    #print('Draw')
                else:
                    tbet1 = bet
                    results['Wins'][g] += 1
                    #print('Player wins')
                if k>m2 and k<=21:
                    tbet2 = -bet
                    results['Loses'][g] += 1
                    #print('Dealer wins')
                elif k==m2:
                    tbet2 = 0
                    results['Draws'][g] += 1
                    #print('Draw')
                else:
                    tbet2 = bet
                    results['Wins'][g] += 1
                    #print('Player wins')
                bet = tbet1 + tbet2
        
        Bank += bet
        bnkrlist.append(Bank)
        results['P/L'][g] = Bank
    bankroll.append(bnkrlist)

bankrolldf = pd.DataFrame(bankroll).T
bankrolldf
resultsdf = pd.DataFrame(results)
resultsdf

bankrolldf.to_csv('Bankroll.csv')
resultsdf.to_csv('Results.csv')

bankrolldf.plot()


f, ax = plt.subplots(figsize=(16,8))
ax.set(xlabel ="Games", ylabel = "Bankroll", title ='Bankroll/Games (1 million plays each game)')
sns.set_style("darkgrid")
plt.legend(loc='upper right')
#sns.color_palette("dark:salmon_r", as_cmap=True)
sns.lineplot(data=bankrolldf)
