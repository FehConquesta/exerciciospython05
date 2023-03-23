aluno =1
for num in range(0,16):

    print("Aluno",aluno)
    nota1 = float(input("Informe a nota do checkpoint 1: "))
    nota2 = float(input("Informe a nota do checkpoint 2: "))
    nota3 = float(input("Informe a nota do checkpoint 3: "))
    media = (nota1+nota2+nota3)/3
    print(f"Sua media ficou {media:.2f}")
    aluno += 1