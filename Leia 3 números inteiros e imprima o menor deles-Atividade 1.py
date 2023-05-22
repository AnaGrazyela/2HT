numero1 = float(input("Digite o Primeiro número:  "))
numero2 = float(input("Digite o segundo número:   "))
numero3 = float(input("Digite o terceiro número:  "))
if numero1 < numero2 and numero1 < numero3:
    print(numero1, numero2, numero3, " e o menor número é: ", numero1)
elif numero2<numero1 and numero2<numero3:
    print(numero1, numero2, numero3, " e o menor número é: ", numero2)
elif numero3<numero1 and numero3<numero2:
    print(numero1, numero2, numero3, " e o menor número é: ", numero3)
