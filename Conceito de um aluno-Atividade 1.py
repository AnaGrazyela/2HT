print("Veja sua média!","\n")
nota1 = float(input("Digite sua primeira nota:  "))
if nota1 == 10:
    print("Excelente","\n")
elif nota1>=8 and nota1<9.9:
    print("Ótimo")
elif nota1>=7 and nota1<7.9:
    print("Bom","\n")
elif nota1>=5 and nota1<6.9:
    print("Regular","\n")
else:
    print("insuficiente","\n")
nota2 = float(input("Digite sua segunda nota:  "))
if nota2 == 10:
    print("Excelente","\n")
elif nota2>=8 and nota2<9.9:
    print("Ótimo","\n")
elif nota2>=7 and nota2<7.9:
    print("Bom","\n")
elif nota2>=5 and nota2<6.9:
    print("Regular","\n")
else:
    print("insuficiente","\n")
nota3 = float(input("Digite sua terceira nota:  "))
if nota3 == 10:
    print("Excelente","\n")
elif nota3>=8 and nota3<9.9:
    print("Ótimo","\n")
elif nota3>=7 and nota3<7.9:
    print("Bom","\n")
elif nota3>=5 and nota3<6.9:
    print("Regular","\n")
else:
    print("insuficiente","\n")
nota4 = float(input("Digite sua quarta nota:  "))
if nota4 == 10:
    print("Excelente","\n")
elif nota4>=8 and nota4<9.9:
    print("Ótimo","\n")
elif nota4>=7 and nota4<7.9:
    print("Bom","\n")
elif nota4>=5 and nota4<6.9:
    print("Regular","\n")
else:
    print("insuficiente","\n")
media = (nota1+nota2+nota3+nota4)/4
print("sua media escolar é: ", media)
if media>8:
    print("Aprovado!","\n")
elif media<7.9 and media>5:
    print("Em recuperação!","\n")
else:
    print("Reprovado!","\n")
