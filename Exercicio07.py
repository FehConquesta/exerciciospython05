cont = 0
num = int(input("Escreva um numero inteiro e positivo: "))
valor= 0
for cont in range(1,11):
    valor = num*cont
    print(num,"X", cont,"=",valor)