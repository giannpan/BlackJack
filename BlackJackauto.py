from random import randint
import time
import pandas as pd
import numpy as np
import seaborn as sns

columns = [2,3,4,5,6,7,8,9,10,'A']
index = [8,9,10,11,12,13,14,15,16,17,18,19,20,'A,2','A,3','A,4','A,5','A,6','A,7','A,8','2,2','3,3','4,4','5,5','6,6','7,7','8,8','9,9','10,10']

df = pd.DataFrame(columns=columns,index=index)
dfs = pd.DataFrame(columns=columns,index=index)


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

for i in range (10):
    pwins = False
    print(f'Your bank is {Bank}')
    playerplay = True
    dealerplay = True
    sp = False
    
    def deal(ph,dh,dk):
        ph.append(dk.pop(randint(0,len(dk)-1)))
        dh.append(dk.pop(randint(0,len(dk)-1)))
        ph.append(dk.pop(randint(0,len(dk)-1)))
        dh.append('?')
    
    def hit(hand,dk):
        if hand[1] == '?':
            hand[1] = dk.pop(randint(0,len(dk)-1))
            lst = list(map(lambda x: x[0],hand))
            if lst.count('A')>1:
                hand[lst.index('A')][0]='A1'
            q = sum(list(map(lambda x: values[x[0]],hand)))
#           phands(dealerhand,playerhand)
        else:
            hand.append(dk.pop(randint(0,len(dk)-1)))
            lst = list(map(lambda x: x[0],hand))
            if lst.count('A')>1:
                hand[lst.index('A')][0]='A1'
                q = sum(list(map(lambda x: values[x[0]],hand)))
            else:
                qtemp = sum(list(map(lambda x: values[x[0]],hand)))
                if qtemp>21 and 'A' in lst:
                    hand[lst.index('A')][0]='A1'
                    q = sum(list(map(lambda x: values[x[0]],hand)))
                else:
                    q = sum(list(map(lambda x: values[x[0]],hand)))
#            phands(dealerhand,playerhand)
        return q
    
        
    bet = 100    
    playerhand = []
    dealerhand = []
    deck=[[i,j] for i in cards for j in suites]
    deal(playerhand,dealerhand,deck)
#    phands(dealerhand,playerhand)
    
    lsp = list(map(lambda x: x[0],playerhand))
    b = dealerhand[0][0]
    if 'A' in lsp or lsp[0]==lsp[1]:
        a = ','.join(sorted(lsp,reverse = True))
    else:
        a = sum(list(map(lambda x: values[x],lsp)))
    if b == 'A':
        pass
    else:
       b = values[b]

    
    # Case when the player has BlackJack
    if 'A' in [playerhand[0][0],playerhand[1][0]] and any(i in [playerhand[0][0],playerhand[1][0]] for i in ['10','J', 'Q','K']):
        print('BlackJack')
        bet *= 1.5
        pwins = True
        dealerplay = False
        playerplay = False
    
    
    # All other cases
    m = sum(list(map(lambda x: values[x[0]],playerhand)))
    while m<17:
        m = hit(playerhand,deck)
    if m>21:
        dealerplay = False
        bet = -bet
    
    
    if dealerplay:
        k = hit(dealerhand,deck)
        # Dealers hand
        while k<17:
            k = hit(dealerhand,deck)
        
        if k>m and k<=21:
            bet = -bet
        elif k==m:
            bet = 0
        else:
            bet = bet
            pwins = True
    Bank += bet
    try:
        if df.loc[a,b] is np.nan:
            df.loc[a,b] = 1
        else:
            df.loc[a,b] += 1
        if pwins == True:
            if dfs.loc[a,b] is np.nan:
                dfs.loc[a,b] = 1
            else:
                dfs.loc[a,b] += 1
    except:
        pass

df
dfs
playerhand
dealerhand
pwins
bet
ddf = dfs/df
ddf
for i in ddf.columns:
    ddf[i] = pd.to_numeric(ddf[i],errors = 'coerce')
sns.heatmap(data = ddf)
ddf.info()
ddf.columns
