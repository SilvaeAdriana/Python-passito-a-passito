#alternativa 1
def épar(x):
    return(x%2==0)
print(épar(3)) #retorna False
print(épar(4)) #retorna True

#alternativa 2
#usuário insere número
numero=int(input('Insira um número:'))
def épar(x):
    return(x%2==0)
print(épar(numero))
