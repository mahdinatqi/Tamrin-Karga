check_claim = {'A':{'c1','b1', 0},
               'B':{'d0','a0','b0'},
               'C':{'a1','b0','c1'},
               'D':{'d1','d0','a1'}}

i = j =k = z = 0
for K , V in check_claim.items():
    for v in V:
        if v == 'a0':
            i-=1
        elif v == 'a1':
            i+=1
        elif v == 'b0':
            j-=1
        elif v == 'b1':
            j+=1
        elif v == 'c0':
            k-=1
        elif v == 'c1':
            k+=1
        elif v == 'd0':
            z-=1
        elif v== 'd1':
            z+=1
        else:
            continue
tef = {'A':i,'B':j,'C':k,'D':z}
max = 0
for k , v in tef.items():
    if max < v:
        max = v
    else:
        continue
for t,s in tef.items():
    if s == max:
        print(f"{t} is the Teaf!")