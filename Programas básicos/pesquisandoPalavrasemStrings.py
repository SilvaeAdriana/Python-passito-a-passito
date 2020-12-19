nome='Adriana da Silva'
#PESQUISANDO PALAVRAS EM STRINGS
nome.startswith('Adriana')#para chamar...return TRUE
nome.endswith('Silva') #return True
nome.lower() #retorna a string com todos os caracteres minúsculos
nome.upper() #retorna a string com todos os caracteres minusculos
nome.lower().startswith('adriana')#retorna TRUE
'Berlin' in nome #pergunta se a string apresentada está dentro de outra antes informada retun FALSE
'Berlin' not in nome #returna TRUE

#usar lower ou upper antes de pesquisar um nome ajuda ao PY
#não diferenciar maiusculas de minusculas
'berlin' in nome.lower()  #return FALSE