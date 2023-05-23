c = float(input("Escreva seu codigo: --> "))
n = float(input("Escreva sua horas trabalhadas: --> "))
valor_numero_horas = n*10
if valor_numero_horas > 50:
    resto1 = n-50
    valor_do_resto = resto1*20
    print("o seu salario é: ", valor_numero_horas, "valor do excesso é: ", valor_do_resto)
else:
    print("Sem excesso!")
