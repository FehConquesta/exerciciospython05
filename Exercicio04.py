num =0
cont= 0
soma = 0
for cont in range(1,11):
    num = float(input("informe um numero: "))
    if(num < 40):
        soma = soma + num
print("Soma dos numeros menor que quarenta :",soma)