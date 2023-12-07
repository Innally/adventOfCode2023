
all_list=[]
gear_pos=[]
final_sum=0
length=0
def check_pos(gear_pos):
    x,y=gear_pos
    return[[x-1,y-1],[x,y-1],[x+1,y-1],[x-1,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]

def recursive_search(tc,sum,base):
    x,y=tc
    if x<0 or x>colnum-1 or y<0 or y>colnum-1:
        return sum
    if all_list[x][y].isnumeric():
        sum+=base*int(all_list[x][y])
        all_list[x][y]='.'
        if all_list[x][y-1].isnumeric() and all_list[x][y+1].isnumeric() and y-1>=0 and y+1<colnum:
            sum= int(all_list[x][y+1])+sum*10+int(all_list[x][y-1])*100
            all_list[x][y-1]='.'
            all_list[x][y+1]='.'
        elif all_list[x][y-1].isnumeric() and y-1>=0:
            sum=recursive_search([x,y-1],sum,base*10)
        elif all_list[x][y+1].isnumeric() and y+1<colnum:
            sum*=10
            sum= recursive_search([x,y+1],sum,base)
        return sum
    else:
        return sum

with open('adventofcode/DAY3/data1','r') as f:
    sum=0
    row=0
    for line in f.readlines():
        all_list.append(list(line))
        for col,str in enumerate(line):
            if str.isnumeric()==False and str!='.' and str!='\n':
                gear_pos.append([row, col])
        row+=1
colnum=len(all_list[0])
rownum=len(all_list)
# print(all_list)
# print(gear_pos)
for gp in gear_pos:
    to_check=check_pos(gp)
    for tc in to_check:
        final_sum+=recursive_search(tc,0,1)
        
print (final_sum)