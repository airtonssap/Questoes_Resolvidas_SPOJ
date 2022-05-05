#Local onde vou armazenar às cédulas BITs
listaprincipal = list()
listasecundaria = list()

#Entrada de valores
while True:
    dinheiro = int(input())
    
    #Parada do loop
    if dinheiro == 0:
        break
    
    #Minimizando às cédulas
    #Notas de 50
    qntcedula = dinheiro//50
    dinheiro -= (qntcedula * 50)
    listasecundaria.append(qntcedula)
    
    #Notas de 10
    qntcedula = dinheiro//10
    dinheiro -= (qntcedula * 10)
    listasecundaria.append(qntcedula)
    
    #Notas de 5
    qntcedula = dinheiro//5
    dinheiro -= (qntcedula * 5)
    listasecundaria.append(qntcedula)
    
    #Notas de 1
    qntcedula = dinheiro//1
    dinheiro -= (qntcedula * 1)
    listasecundaria.append(qntcedula)
    
    listaprincipal.append(listasecundaria.copy())
    listasecundaria.clear()

print(listaprincipal)
#Saída do sistema
for indice, cedulas in enumerate(listaprincipal):
    print(f'Teste {indice+1}')
    print(f'{cedulas[0]} {cedulas[1]} {cedulas[2]} {cedulas[3]}\n')
 