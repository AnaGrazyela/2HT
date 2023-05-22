print("==MENU==\n")
print("Verde = R$10.00\n")
print("Azul = R$20.00\n")
print("Amarelo = R$30.00\n")
print("Vermelho = R$40.00\n")
ler = input("Escreva a cor para descobrir o valor:  ")
if ler == "Verde" or ler == "VERDE" or ler == "verde":
    print("Valor é R$10.00")
elif ler == "Azul" or ler == "AZUL" or ler == "azul":
    print("Valor é R$20.00")
elif ler == "Amarelo" or ler == "AMARELO" or ler == "amarelo":
    print("\nValor é R$30.00")
else:
    print("\nValor é R$40.00")
