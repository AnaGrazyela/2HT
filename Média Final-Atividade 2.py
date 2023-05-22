n1 = float(input("Digite sua 1° nota: "))
n2 = float(input("Digite sua 2° nota:  "))
n3 = float(input("Digite sua 3° nota:  "))
n4 = float(input("Digite sua 4° nota:  "))
mediaAritmetica = (n1+n2+n3+n4)/4
print("Sua média é: ", round(mediaAritmetica,1))
if mediaAritmetica == 0 in mediaAritmetica <=3.9:
    print("Em processo de Aprendizagem (Reprovado)")
elif mediaAritmetica == 4 in mediaAritmetica <= 7.9:
    print("Recuperação")
else:
    print("Aprovado!")
