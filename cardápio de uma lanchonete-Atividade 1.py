print("=========================================\n")
print(" Seja bem vindo a lanchonete da Grazy")
print("\n=========================================")
print("           | Menu |\n")
print("|Comida|   |Código|   |Valor|  ","\n")
print("Cachorro-quente = 100 = R$1,20\n")
print("Bauru = 101 = R$1,30\n")
print("Hambúrguer = 102 = R$1,20\n")
print("Cheeseburguer = 103 = R$1,30\n")
print("Refrigerante = 104 = R$1,00\n")
pedido = int(input("Qual é seu pedido?    "))
if pedido == 100:
    print("\nDeu o valor de R$1,20","\n")
elif pedido == 101:
    print("\nDeu o valor de R$1,30","\n")
elif pedido == 102:
    print("\nDeu o valor de R$1,20","\n")
elif pedido == 103:
    print("\nDeu o valor de R$1,30","\n")
elif pedido == 104:
    print("\nDeu o valor de R$1,00","\n")
else:
    print("\nEste código não está registrado na tabela","\n")

print("Obrigada,volte sempre!","\n")