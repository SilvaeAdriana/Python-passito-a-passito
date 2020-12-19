#pesquisa a posição que o termo aparece na string
frase='um tigre,dois tigres, três tigres'
p=0
while(p>-1):
    p=frase.find('tigre',p)
    if p>=0:
       print ('Posição: %d' %p)
       p+=1
#imprime:
'''Posição: 3
Posição: 14
Posição: 27'''