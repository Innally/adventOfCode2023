cards=[]
with open('adventofcode/DAY4/data2','r') as f:
    for i,line in enumerate(f.readlines()):
        line = line.split(':')[1]
        t_card={}
        t_card['win'],t_card['mine']=line.split('|')
        t_card['win']=[int(i) for i in t_card['win'].split()]
        t_card['mine']=[int(i) for i in t_card['mine'].split()]
        cards.append(t_card)

card_won=[1]*len(cards)
for i,c in enumerate(cards):
    match_card=0
    for wn in c["win"]:
        if wn in c['mine']:
            match_card+=1
    print(match_card)
    if match_card>0:
        for j in range(match_card):
            card_won[i+j+1]+=1*card_won[i]
print(card_won)
print(sum(card_won))