cards=[]
with open('adventofcode/DAY4/data1','r') as f:
    for i,line in enumerate(f.readlines()):
        line = line.split(':')[1]
        t_card={}
        t_card['win'],t_card['mine']=line.split('|')
        t_card['win']=[int(i) for i in t_card['win'].split()]
        t_card['mine']=[int(i) for i in t_card['mine'].split()]
        cards.append(t_card)
# print(cards)


sum=0
for c in cards:
    match_card=-1
    for wn in c["win"]:
        if wn in c['mine']:
            match_card+=1
    print(match_card)
    if match_card>=0:
        sum+=pow(2,match_card)    
    
print(sum)    
    