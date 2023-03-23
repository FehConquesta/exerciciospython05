cont = 0
soma = 0
media = 0

for cont in range(1,9):
    num = int(input("Digite um numero inteiro: "))
    soma = soma + num

media = soma/8
print("Soma de todos os numeros: ",soma)
print("Media dos numeros: ",media)