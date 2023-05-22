numero1 = float(input("Digite o primeiro: "))
numero2 = float(input("Digite o primeiro: "))
numero3 = float(input("Digite o primeiro: "))
if numero1<numero2 and numero1<numero3:
    print(numero1,",", numero2,",", numero3, ", O menor numero é: ", round(numero1,2))
elif numero2<numero1 and numero2<numero3:
	print(numero1, numero2, numero3, "O menor numero é: ", round(numero2,2))
else:
	print(numero1, numero2, numero3, "O menor numero é: ", round(numero3,2))
