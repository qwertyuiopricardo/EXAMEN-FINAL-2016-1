for i in range(1,1001):
    cont=0
    for j in range(1, i+1):
        if i%j==0:
            cont=cont+1
print(cont)
