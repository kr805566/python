n=int(input("輸入"))
for i in range(1,n+1): #1~N
    S=""
    k=0
    for j in range(1,i+1): #1~i
        k+=1
        S+=str(k)
       
    print(S)