kilo = float(input("Coloque os kilos do peixe na balança: --> "))
if kilo <= 50:
    print("Não pagará multa!")
elif kilo > 50:
    excesso = (kilo-50)*4
    print("O valor do excesso é de: R$", round(excesso,2), " reais")
