from heapq import nlargest


fname = input('Enter name of file: ')
if len(fname) < 1: fname = 'clown.txt'
hand=open(fname)
di = dict()
for lin in hand:
    lin=lin.rstrip()
    wds=lin.split()
    for w in wds:
        di[w]= di.get(w,0)+ 1

nlargest-1
theword=None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest= v
        theword= k

print('Done',theword,largest)        
