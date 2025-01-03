listofprimes=[]
primesupto =  input("primes up to where")
for i in range(int(primesupto)):
    x=0
    for j in range(i):
        if j > 0:
            if i%j == 0:
                x+=1
    if x == 1:
        print(i,",",end="")
