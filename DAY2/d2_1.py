
red=12
green=13
blue=14

with open('data1','r') as f:
    sum=0
    id = 1
    for line in f.readlines():
        tb=tg=tr=0
        line = line.replace(';', '')
        line = line.replace(',', '')
        con=line.split()
        del con[0]
        del con[0]
        print(con)
        for i in range(int(len(con)/2)):
            if con[i*2+1] == "blue" and int(con[i*2])>tb:
                tb= int(con[i*2])
            elif con[i*2+1] == "red" and int(con[i*2])>tr:
                tr= int(con[i*2])
            elif con[i*2+1] == "green" and int(con[i*2])>tg:
                tg= int(con[i*2])
        if tb<=blue and tr<=red and tg<=green:
            sum+=id
        id+=1
        
print(sum)