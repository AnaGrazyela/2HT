valor = float(input("Digite o valor em dólar ou euro que deseja converter para reais: "))
moeda = input("Tecle 'a' para dólar ou 'b' para Euro: ")
if moeda == 'a':
    conversao = 5.01
elif moeda == 'b':
    conversao = 5.49
else:
    print("Essa moeda não foi declaradas acima.")
    exit(0)
resultado = valor * conversao
print(f"O valor de {valor:.2f} {moeda.upper()} em reais é de {resultado:.2f} reais.")
