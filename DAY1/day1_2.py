sum=0
with open("day1_2_data",'r') as f:
    for i in f.readlines():
        i=i.replace('one', 'one1one')
        i=i.replace('two', 'two2two')
        i=i.replace('three', 'three3three')
        i=i.replace('four', 'four4four')
        i=i.replace('five', 'five5five')
        i=i.replace('six', 'six6six')
        i=i.replace('seven', 'seven7seven')
        i=i.replace('eight', 'eight8eight')
        i=i.replace('nine', 'nine9nine')
        i=i.replace('zero', 'zero0zero')
        s= None
        e= None
        for j in i:
            if j.isnumeric():
                if s==None:
                    s=int(j)
                else:
                    e=int(j)
        if e ==None:
            e=s 
        print(s*10+e)
        sum+= s*10+e
        
    
print(sum)