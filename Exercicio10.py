cont = 0
soma = 0
max = 0
min = 0
for cont in range (1,6):
    print("Funcionario ",cont)
    nome = input("Informe seu nome:")
    salario = float(input("Informe seu salario"))

    if(salario > max):
        maxNome = nome
        max = salario
    else:
        minNome = nome
        min = salario



    soma = soma+ salario

print("A media do salario da empresa XXX é: ",soma/5)
print("O menor salario é do ", minNome," que é R$",min)
print("O maior salario é do ",maxNome, " que é R$", max)


