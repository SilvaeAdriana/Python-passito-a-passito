nota=[5,6,7,8,7]
soma=0
x=0
while x<5:
    soma+=nota[x] #equivale a soma=soma+nota[x]
    x+=1 #equivale a x=x+1
print("Média: %5.2f"%(soma/x))