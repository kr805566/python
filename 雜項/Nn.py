def 自戀數(N):
    
    個=N%10
    十=int((N%100-個)/10)
    百=int((N-十*10-個)/100)
    
    總和=pow(個, 3)+pow(十, 3)+pow(百, 3)
    
    if (N==總和):
        print("他很自戀")
    else:
        print("他不自戀")
    
    
n=int(input("請輸入N:"))
自戀數(n)

