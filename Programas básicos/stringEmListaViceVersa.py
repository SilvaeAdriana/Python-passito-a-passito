s="Alô, mundo"
print (s[0])
#imprime A

#como imprimir uma string como uma lista, caractere a caractere
#list transforma string->lista
s=list('Alô,mundo')
print(s)
#imprime:['A', 'l', 'ô', ',', 'm', 'u', 'n', 'd', 'o']

#join transforma lista->string

t="".join(s)
print(t)
#imprime Alô,mundo