seed=0
store=0
seedsoil=[] # des source range 1
soilfert=[] # 2
fertwater=[]
waterlight=[]
lighttemp=[]
temphumi=[]
humiloc=[] # 7
with open('adventofcode/DAY5/data1','r') as f:
    for i,line in enumerate(f.readlines()):
        if i==0:
            seed = line.split(':')[1].split()
            seed = [int(i) for i in seed]
        elif line=='\n':
            continue
        else:
            if line=="seed-to-soil map:\n":
                store=1
                continue
            elif line=="soil-to-fertilizer map:\n":
                store=2 
                continue
            elif line=="fertilizer-to-water map:\n":
                store=3
                continue
            elif line=="water-to-light map:\n":
                store=4
                continue
            elif line=="light-to-temperature map:\n":
                store=5
                continue
            elif line=="temperature-to-humidity map:\n":
                store=6
                continue
            elif line=="humidity-to-location map:\n":
                store=7
                continue
            
        if store==1:
            seedsoil.append([int(i) for i in line.split()])
        elif store==2:
            soilfert.append([int(i) for i in line.split()])
        elif store==3:
            fertwater.append([int(i) for i in line.split()])
        elif store==4:
            waterlight.append([int(i) for i in line.split()])
        elif store==5:
            lighttemp.append([int(i) for i in line.split()])
        elif store==6:
            temphumi.append([int(i) for i in line.split()])
        elif store==7:
            humiloc.append([int(i) for i in line.split()])

seed_list=[]
nominal_min=seed[0]
for i in range(int(len(seed)/2)):
    if seed[i*2]<nominal_min:
        nominal_min=seed[i*2]
    


loc_list=[]
for i in range(int(len(seed)/2)):
    for r in seedsoil: 
        if seed[i*2]>r[1]+r[2] or seed[i*2+1]< r[1]: #no intersection
            continue
        if seed[i*2]< r[1]+r[2] and seed[i*2] > r[1]:
            t=range(r[1]+r[2], seed[i*2]-r[1]-r[2])
        else:
            t=range(r[1], seed[i*2]+seed[i*2]-r[1])
        
        if t in range(r[1],r[1]+r[2]): # have mapping
            step=t-r[1]
            t=r[0]+step
            break
    for r in soilfert:
        if t in range(r[1],r[1]+r[2]): # have mapping
            step=t-r[1]
            t=r[0]+step
            break
    for r in fertwater:
        if t in range(r[1],r[1]+r[2]): # have mapping
            step=t-r[1]
            t=r[0]+step
            break
    for r in waterlight:
        if t in range(r[1],r[1]+r[2]): # have mapping
            step=t-r[1]
            t=r[0]+step
            break
    for r in lighttemp:
        if t in range(r[1],r[1]+r[2]): # have mapping
            step=t-r[1]
            t=r[0]+step
            break
    for r in temphumi:
        if t in range(r[1],r[1]+r[2]): # have mapping
            step=t-r[1]
            t=r[0]+step
    for r in humiloc:
        if t in range(r[1],r[1]+r[2]): # have mapping
            step=t-r[1]
            t=r[0]+step
            break
    loc_list.append(t)
    
print(min(loc_list))