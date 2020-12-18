lista=[1,8,6]
p=int(input("Insira um número:"))
for e in lista: #e ou i,usado mais frequentemente, representa qualquer elemento da lista
    if e==p:
        print("Elemento encontrado!")
        break
else:
    print("Elemento não encontrado")
